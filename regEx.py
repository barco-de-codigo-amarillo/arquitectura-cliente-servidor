"""
A regular expression or RegEx is a special text string that helps to find patterns in data
Methods in the 're' module:
re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string

^: Indica el inicio de una línea [INDEX].
$: Indica el final de una línea.
\d: Busca cualquier número/dígito (del 0 al 9).
\w: Busca cualquier carácter alfanumérico (letras, números y guion bajo).
+: Indica que el símbolo anterior se puede repetir 1 o más veces.
"""

# Encontrar todas las palabras que empiezan con una letra (re.findall)
import re

texto = "Finlandia y Estonia son países del norte, pero Francia está en el oeste."

# Patrón: \b (inicio de palabra), F (letra F), \w+ (cualquier letra que siga)
paises_con_f = re.findall(r'\bF\w+', texto)

print(paises_con_f)
# Salida: ['Finlandia', 'Francia']
print('***********************************************')


# Validar el formato de un Correo Electrónico (re.match)
import re

def validar_email(email):
    # Patrón estándar para correos electrónicos
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' # el '^' es redundante por el siguiente uso de re.match()
    
    if re.match(patron, email):
        return True
    return False

# Pruebas
print(validar_email("alumno_m@email.com"))  # Salida: True
print(validar_email("correo-invalido.com"))   # Salida: False
print('***********************************************')


# Extraer números de un texto plano (re.findall)
import re

registro_servidor = "Error 404: El usuario 1025 intentó acceder 3 veces sin éxito."

# Patrón: \d+ busca cualquier secuencia de uno o más dígitos numéricos
numeros_extraidos = re.findall(r'\d+', registro_servidor)

print(numeros_extraidos)
# Salida: ['404', '1025', '3']
print('***********************************************')


# re.search() — Buscar la primera coincidencia en cualquier parte del texto
import re

frase = "El código de error crítico es 500 en el servidor."

# Buscamos el primer número de 3 dígitos (\d{3})
coincidencia = re.search(r'\d{3}', frase)

if coincidencia:
    print(f"Encontrado: {coincidencia.group()}")  # Extrae el texto real
    print(f"Posición en el texto: del carácter {coincidencia.start()} al {coincidencia.end()}")
# Salida: Encontrado: 500
print('***********************************************')

# re.sub() — Buscar y Reemplazar texto (Sustitución)
import re

texto_sucio = "Mi contraseña secreta es abcd123 y mi pin es 9988."

# Reemplazamos cualquier secuencia de dígitos (\d+) por la palabra [CENSURADO]
texto_limpio = re.sub(r'\d+', '[CENSURADO]', texto_sucio)

print(texto_limpio)
# Salida: Mi contraseña secreta es abcd[CENSURADO] y mi pin es [CENSURADO].
print('***********************************************')

# re.split() — Dividir un texto usando un patrón complejo
import re

# El texto tiene comas, puntos y espacios mezclados como separadores
linea_datos = "Estonia,Finland;Sweden.Denmark Norway"

# Rompemos la cadena usando como separador una coma, un punto, un punto y coma o un espacio
lista_paises = re.split(r'[,;.\s]+', linea_datos)

print(lista_paises)
# Salida limpia: ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway']
print('***********************************************')

# re.compile() — Reutilizar y optimizar un patrón
import re

# Compilamos el patrón una sola vez fuera del bucle
patron_comprobacion = re.compile(r'^[A-Z]') # Busca si empieza por mayúscula

paises = ["Finlandia", "estonia", "Suecia", "noruega"]

for p in paises:
    if patron_comprobacion.match(p):
        print(f"Correcto: {p}")
    else:
        print(f"Invalido (debe empezar con mayúscula): {p}")

print('***********************************************')

