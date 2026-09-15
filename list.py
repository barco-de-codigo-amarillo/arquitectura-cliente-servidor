# Generación de listas
# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']
print('**********************************************')

# Second way: list comprehension
lst = [i for i in language] # guarda como lista cada elemento en la varibale; recorre la variable 'language' letra por letra y guarda la letra actual en la variable temporal 'i'(2º 'i'); 'i'(1er 'i') valor que guarda en la lista; [...] agrupan los elementos individuales en una lista;
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']
print('**********************************************')

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)] # genera una tupla(elementos inmutables) con el formato '(i, i * i)' por cada elemento en el rango 0-11
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
print('**********************************************')

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0] # genera una lista por cada elemento de la lista numbers que sea par y positivo
print(positive_even_numbers) # [4, 6, 8, 10]
print('**********************************************')

# Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # matriz
flattened_list = [ number for row in list_of_lists for number in row] # genera una lista de elementos(number) por cada elemento en el fila(row) de la matriz y por cada elemento dentro de la fila
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('**********************************************')




"""
LAMBDA
"""

# function in traditional mode
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
print('***********************************************')

# the lambda function equivalent
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5
print('***********************************************')


# Lambda function inside another function
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets, the first is 'x' and the second is 'n'
print(cube)          # 8
two_power_of_five = power(2)(5) # (x)(n)
print(two_power_of_five)  # 32