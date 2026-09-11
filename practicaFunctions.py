# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to_fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    farenheit = celsius * (9/5) + 32
    return farenheit

print(convert_celsius_to_fahrenheit(12))
print('***********************************************************')

# Función que recibe 2 argumentos
def calcular(f, x):
    return f(x)

# Función convertir Fahrenheit a Celsius
def convert_fahrenheit_to_celsius(fahrenheit):
    celsius =  fahrenheit - 32 * (5/9)
    return celsius

print(calcular(convert_fahrenheit_to_celsius, 99))
print('***********************************************************')


# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def season(month):
    # Diccionario para traducir el número del mes a su nombre en texto
    meses_por_numero = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    
    # Si nos pasan un número (ej. 3), lo convertimos a su texto ('March')
    if type(month) is int:
        month = meses_por_numero.get(month)
        
    # Clasificamos el mes en su estación correspondiente
    if month in {'March', 'April', 'May'}:
        return 'Spring'
    elif month in {'June', 'July', 'August'}:
        return 'Summer'
    elif month in {'September', 'October', 'November'}:
        return 'Autumn'
    elif month in {'December', 'January', 'February'}:
        return 'Winter'
    else:
        return 'Invalid Month'

# --- EJEMPLOS DE USO ---
print(season('March'))  # Resultado: Spring (Funciona con texto)
print(season(3))        # Resultado: Spring (Funciona con número)
print(season(7))        # Resultado: Summer


# escribir una función que acepte cuatro operaciones aritméticas:
# sumar, restar, multiplicar y dividir a través de una petición 
# previa a usuario por opciones: ..."pulse 's' para sumar", "pulse 'r' para restar", ... . Si el usuario pulsa la opción adecuada se realiza
# la operación con los dos argumentos adicionales del usuario. Sin embargo,
# si el usuario da un input de opción fuera de {"s", "r", "m", "d"} 
# entonces se le indica "el error" y se le ofrece de nuevo el menú de opciones... hasta que haga una petición correcta

def calculate():
    # permitimos infinitos intentos hasta que esté en el diccionario creado la elección de teclado
    while True:
        # diccionario de posible entradas
        operaciones = {'s': 'sumar','r': 'restar', 'm': 'multiplicar', 'd': 'dividir'}

        # entrada de datos del usuario
        dato_usuario = input("pulse 's' para sumar, pulse 'r' para restar, pulse 'm' para multiplicar o pulse 'd' para dividir: ")

        # si se cumple la condición rompe el bucle
        if dato_usuario.lower() in operaciones:
            break

    # Entrada de datos numéricos por teclado
    x = int(input('Introduzca el primer número: '))
    y = int(input('Introduzca el segundo número: '))
            
    # realizamos la operación definida según entrada de teclado
    match dato_usuario.lower():
        case 's':
            return x + y
        case 'r':
            return x - y
        case 'm':
            if x == 0 or y == 0:
                return ('El número debe ser no nulo')
            else:
                return x * y
        case 'd':
            if x == 0 or y == 0:
                return ('El número debe ser no nulo')
            else:
                return x / y
        case _:
            return 'Operación inválida'
    
        
print(calculate())


# Una manera más sencilla
"""
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

sel = int(input("Select operation (1-4): "))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if sel == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif sel == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
elif sel == 3:
    print(n1, "*", n2, "=", mul(n1, n2))
elif sel == 4:
    print(n1, "/", n2, "=", div(n1, n2))
else:
    print("Invalid input")
"""


# Función de asignación de los argumentos variable de entrada de teclado
def entradaVariable():
    # 1. Creamos el conjunto vacío FUERA del while para que no se borre en cada vuelta
    datos_teclado = set()

    while True:
        # Capturamos la entrada y la convertimos a entero
        numero = int(input('Introduce un número para analizar: '))

        if numero <= 45 and numero >= -7:

            # Agregamos el número al conjunto (.add)
            datos_teclado.add(numero)

        # Ahora sí, miramos cuántos elementos ÚNICOS tiene el conjunto
        if len(datos_teclado) == 5:
            break

    print(f"\n¡Perfecto! Ya tenemos los {len(datos_teclado)} números únicos.")

    # 2. Calculamos el promedio del rango de -7 a 45
    suma_total = sum( datos_teclado)
    total_elementos = len( datos_teclado)
    
    promedio = suma_total / total_elementos
    return promedio

# Llamamos a la función
print("El promedio es:", entradaVariable())
