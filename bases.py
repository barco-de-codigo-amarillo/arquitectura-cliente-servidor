# Variables en Python

first_name = 'Barco'
last_name = 'Amarillo'
country = 'Saturno'
city = 'Saturnaria'
age = 1000
number_of_siblings = 2
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Barco', 
    'lastname':'Amarillo', 
    'country':'Saturno',
    'city':'Saturnaria'
    }

# Imprimir los valores almacenados en las variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declarar múltiples variables en una línea

first_name, last_name, country, age, is_married = 'Barco', 'Amarillo', 'Saturno', 1000, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)


# Declarar múltiples variables en una misma línea con diferentes valores
x, y, z = 1, 2, 3
print(x + y + z) # 6


# Desestructuring. Desde aquí lo que va a hacer es sacar cada letra en una variable
language = 'Python'

a,b,c,d,e,f = language # desempaquetar caracteres y asignarlos a variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n




# 'sep' es un parámetro que se utiliza para separar los valores que se imprimen en la misma línea. Por defecto, el valor 
# de 'sep' es un espacio en blanco, pero se puede cambiar a cualquier otro carácter o cadena de caracteres.
print(first_name, last_name, country, age, is_married)


# 'end' es un parámetro que se utiliza para especificar el carácter o cadena de caracteres que se imprimirá al final de
#  la línea. Por defecto, el valor de 'end' es un salto de línea, pero se puede cambiar a cualquier otro carácter o cadena 
# de caracteres.
print(first_name, end='*')

# 'type' es una función que se utiliza para obtener el tipo de dato de una variable o valor
print('El tipo de la variable de un diccionario en el que se recoge la información de la persona es: ', type(person_info))


# 'len' es una función que se utiliza para obtener la longitud de una cadena de caracteres, lista, tupla, diccionario 
# o conjunto.
print(len(first_name) > len(last_name)) # True


# 'isinstance' es una función que se utiliza para comprobar si un objeto es una instancia de una clase o tipo de dato específico.
print(isinstance(first_name, str)) # True


# 'id' es una función que se utiliza para obtener el identificador único de un objeto en memoria.
print(id(first_name)) # 140706091155888


# 'input' es una función que se utiliza para obtener la entrada del usuario desde la consola. La función devuelve una cadena de caracteres.
name = input('What is your name? ')
print('Your name is: ', name)


# 'int' es una función que se utiliza para convertir un valor a un número entero.
num_one = int(input('Enter number one: '))
num_two = int(input('Enter number two: '))
total = num_one + num_two
print('Total: ', total)

# 'float' es una función que se utiliza para convertir un valor a un número decimal.
num_one = float(input('Enter number one: '))
num_two = float(input('Enter number two: '))
total = num_one + num_two
print('Total: ', total)


# 'str' es una función que se utiliza para convertir un valor a una cadena de caracteres.
num_one = str(input('Enter number one: '))
num_two = str(input('Enter number two: '))
total = num_one + num_two
print('Total: ', total)


# 'bool' es una función que se utiliza para convertir un valor a un valor booleano (True o False).
is_true = bool(1)
is_false = bool(0)
print('is_true: ', is_true) # True
print('is_false: ', is_false) # False


# 'list' es una función que se utiliza para convertir un valor a una lista.
num_list = list((1, 2, 3))
print('num_list: ', num_list) # [1, 2, 3]


# 'tuple' es una función que se utiliza para convertir un valor a una tupla.
num_tuple = tuple((1, 2, 3))
print('num_tuple: ', num_tuple) # (1, 2, 3)


# 'set' es una función que se utiliza para convertir un valor a un conjunto.
num_set = set((1, 2, 3))
print('num_set: ', num_set) # {1, 2, 3}


# 'dict' es una función que se utiliza para convertir un valor a un diccionario.
num_dict = dict(name='Barco', age=1000)
print('num_dict: ', num_dict) # {'name': 'Barco', 'age: 1000}


# 'frozenset' es una función que se utiliza para convertir un valor a un conjunto inmutable.
num_frozenset = frozenset((1, 2, 3))
print('num_frozenset: ', num_frozenset) # frozenset({1, 2, 3})


# 'complex' es una función que se utiliza para convertir un valor a un número complejo.
num_complex = complex(1, 2)
print('num_complex: ', num_complex) # (1+2j)


# % para sacar el resto de una división, // para sacar la parte entera de una división y ** para sacar la potencia de un número.
print('Resto de la división: ', 3 % 2) # 1
print('Numero par:', 6%2 == 0) # True
print('Numero impar:', 7%2 != 0) # True
print('Parte entera de la división: ', 3 // 2) # 1
print('Potencia de un número: ', 3 ** 2) # 9


# 'round' es una función que se utiliza para redondear un número decimal a un número entero.
print('Redondear un número decimal: ', round(3.14)) # 3


# 'abs' es una función que se utiliza para obtener el valor absoluto de un número.
print('Valor absoluto de un número: ', abs(-3.14)) # 3.


# 'divmod' es una función que se utiliza para obtener el cociente y el resto de una división.
print('Cociente y resto de una división: ', divmod(3, 2)) # (1, 1)


# 'pow' es una función que se utiliza para obtener la potencia de un número.
print('Potencia de un número: ', pow(3, 2)) # 9


# 'max' es una función que se utiliza para obtener el valor máximo de una lista, tupla o conjunto.
print('Valor máximo de una lista: ', max([1, 2, 3]))


# 'min' es una función que se utiliza para obtener el valor mínimo de una lista, tupla o conjunto.
print('Valor mínimo de una lista: ', min([1, 2, 3]))


# 'sum' es una función que se utiliza para obtener la suma de los valores de una lista, tupla o conjunto.
print('Suma de los valores de una lista: ', sum([1, 2, 3]))


# 'sorted' es una función que se utiliza para ordenar los valores de una lista, tupla o conjunto.
print('Valores ordenados de una lista: ', sorted([3, 2, 1])) # [1, 2, 3]


# 'reversed' es una función que se utiliza para invertir el orden de los valores de una lista, tupla o conjunto.
print('Valores invertidos de una lista: ', list(reversed([1, 2, 3]))) # [3, 2, 1]


# 'enumerate' es una función que se utiliza para obtener el índice y el valor de los elementos de una lista, tupla o conjunto.
for index, value in enumerate([1, 2, 3]):
    print('Index: ', index, 'Value: ', value)


# 'zip' es una función que se utiliza para combinar los valores de dos o más listas, tuplas o conjuntos en una sola lista, tupla o conjunto.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print('Valores combinados de dos listas: ', list(zipped)) # [(1, 'a'), (2, 'b'), (3, 'c')]


# 'map' es una función que se utiliza para aplicar una función a cada elemento de una lista, tupla o conjunto.
def square(x):
    return x ** 2

mapped = map(square, [1, 2, 3])
print('Valores después de aplicar la función: ', list(mapped)) # [1, 4, 9]


# 'filter' es una función que se utiliza para filtrar los elementos de una lista, tupla o conjunto según una condición.
def is_even(x):
    return x % 2 == 0

filtered = filter(is_even, [1, 2, 3, 4, 5, 6])
print('Valores después de filtrar: ', list(filtered)) # [2, 4, 6]


# 'reduce' es una función que se utiliza para reducir los elementos de una lista, tupla o conjunto a un solo valor.
from functools import reduce
def add(x, y):
    return x + y

reduced = reduce(add, [1, 2, 3, 4, 5])
print('Valor después de reducir: ', reduced) # 15

# 'any' es una función que se utiliza para comprobar si al menos uno de los elementos de una lista, tupla o conjunto es verdadero.
print('Al menos uno de los elementos es verdadero: ', any([False, False, True])) # True


# type() es una función que se utiliza para obtener el tipo de dato de un valor o variable.
print('Tipo de dato de un valor: ', type(1)) # <class 'int'>
print('Tipo de dato de una variable: ', type(first_name)) # <class 'str'>
print(type(None))
# es un str que tiene forma de float que viene de un método len()
print((str(float(len('python')))))
# <class 'str'>; siempre tiene que pasar por 'float' para sacarlo finalmente como 'int'
print(type(int(float(str(float(len('python')))))))
