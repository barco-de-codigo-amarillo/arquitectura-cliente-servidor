# Write a function which generates a six digit/character random_user_id
"""
string.ascii_letters: Contiene todas las letras de la a-z y A-Z.
string.digits: Contiene los números del 0-9.
random.choice(): Elige un elemento al azar de la lista o cadena que le pases.
''.join(...): Une todos los caracteres generados en un único string limpio.
"""
import random
import string

def generar_texto_aleatorio(longitud):
    # Combinamos letras y números
    caracteres_posibles = string.ascii_letters + string.digits
    
    # Generamos la lista de caracteres y los unimos en un solo string
    resultado = ''.join(random.choice(caracteres_posibles) for _ in range(longitud))
    return resultado

# Ejemplo: Generar una cadena de 10 caracteres
cadena_aleatoria = generar_texto_aleatorio(10)
print(f"Cadena aleatoria: {cadena_aleatoria}")
print('*********************************************************')




# Second practice
"""
Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters
but it takes two inputs using input(). One of the inputs is the number of characters and the second 
input is the number of IDs which are supposed to be generated.
"""

def user_id_gen_by_user():

    # entrada para la longitud de caracteres
    longitud = int(input('Longitud de la cifra: '))

    # entrada de los dígitos de los IDs
    cracteresIds = input('ID: ')

    # Generamos la lista de caracteres y los unimos en un solo string
    ids = ''.join(random.choice(cracteresIds) for _ in range(longitud))
    return ids


id_aleatorio = user_id_gen_by_user()
print(f"ID que se ha generado desde la aleatoriedad: {id_aleatorio}")
print('*********************************************************')


# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)

from random import randint

def rgb_color_gen():
    # Generamos 3 números enteros independientes, cada uno entre 0 y 255
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    # Devolvemos los 3 valores estructurados como una tupla; las tuplas conllevan menos entropía
    return (r, g, b)

# Para ejecutar la función debemos añadir los paréntesis () al llamarla
print(rgb_color_gen())
print('*******************************************')




"""
r: Es el nombre de tu variable (que contiene un número entero, por ejemplo, el 7).
:: Indica que vas a aplicar un formato especial a esa variable.
3d: Le dice a Python que el valor es un número entero (decimal) y que obligatoriamente debe ocupar
un ancho mínimo de 3 caracteres.
0: Le dice a Python que si el número no llega a los 3 caracteres, rellene los espacios vacíos del lado izquierdo con ceros.
"""

def rgb_color_gen():
    # 1. Inicializamos como números enteros (int)
    r = 999
    g = 999
    b = 999
    
    # 2. Los bucles evalúan enteros contra enteros
    while r > 255:
        # Generamos texto, pero lo convertimos a INT inmediatamente con int()
        r = int(''.join(random.choice(string.digits) for _ in range(3)))
        
    while g > 255:
        g = int(''.join(random.choice(string.digits) for _ in range(3)))
        
    while b > 255:
        b = int(''.join(random.choice(string.digits) for _ in range(3)))

    # 3. Al final, unimos todo en el formato de texto
    rgb_digits = f"{r:03d},{g:03d},{b:03d}"
    return rgb_digits

print(rgb_color_gen())
