const solanaClient = await createSolanaClient({
  dapp: {
    name: 'My Node.js Solana App',
    url: 'https://myapp.com', 
  },
  api: {
    supportedNetworks: getInfuraRpcUrls({
      infuraApiKey: 'YOUR_INFURA_API_KEY',
      networks: ['devnet'],
    }),
  },
});   