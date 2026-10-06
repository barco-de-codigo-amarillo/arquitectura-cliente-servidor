// index.mjs
import { createSolanaClient, getInfuraRpcUrls } from '@metamask/connect-solana'

const SOLANA_DEVNET = 'solana:ETQ2d9Jk8VqSvJQaD4d6x1YnH3zWmKpL' // scope de devnet

const solanaClient = await createSolanaClient({
  dapp: {
    name: 'My Node.js Solana App',
    url: 'https://myapp.com',
  },
  api: {
    supportedNetworks: getInfuraRpcUrls({
      infuraApiKey: process.env.INFURA_API_KEY,
      networks: ['devnet'],
    }),
  },
})

// 1. Escuchar cambios de sesión
let session
solanaClient.core.on('wallet_sessionChanged', s => {
  session = s
})

// 2. CONECTAR (aquí aparece un QR que escaneas con MetaMask móvil)
await solanaClient.core.connect([SOLANA_DEVNET], [])

// 3. Obtener la dirección
const accounts = session?.sessionScopes?.[SOLANA_DEVNET]?.accounts ?? []
const address = accounts[0]?.split(':').pop()
console.log('Conectado:', address)

// 4. (Opcional) Firmar un mensaje
const message = Buffer.from('Hola desde Node.js!', 'utf8').toString('base64')
const result = await solanaClient.core.invokeMethod({
  scope: SOLANA_DEVNET,
  request: {
    method: 'signMessage',
    params: { account: { address }, message },
  },
})
console.log('Firma:', result.signature)

// 5. Desconectar
await solanaClient.disconnect()   