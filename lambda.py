# Una función lambda es una función anónima
"""
La sintaxis siempre es: lambda argumentos: expresion
lambda: Es la palabra clave que le avisa a Python lo que vas a hacer.
(argumentos)x (o cualquier variable): Son los parámetros que recibe (puede recibir varios, separados por comas, ej: lambda x, y: x + y).
:: Separa los argumentos de la acción.
(expresión)x + 10: Es lo que la función hace y devuelve automáticamente (no necesitas escribir la palabra return).
"""
sumar_diez_lambda = lambda x: x + 10

print(sumar_diez_lambda(5)) # Resultado: 15


# **************************************************************************************************************************************

# "Toma un diccionario 'country', y usa su clave 'population' para ordenar". Muy utilizado en .sort(key=...) para ordenar en una función lambda
key = lambda country: country['population']


# **************************************************************************************************************************************

"""
.items(), transforma el diccionario en una lista de parejas (tuplas).
key=lambda x: x[1l dice a Python con respecto a qué quieres ordenar. x[1] ordena fijándose en el número de países, no en el nombre del idioma
reverse=True, obligas a ordenar de mayor a menor
[:10] slice de los 10 primeros
"""
conteo_idiomas = {} # es un diccionario que supuestamente estamos llenando de pares clave-valor y que luego queremos comparar

top_10 = sorted(conteo_idiomas.items(), key=lambda x: x[1], reverse=True)[:10]

# REdundacia: es la cualidad de que no se va ha alterar una tabla su info 
