# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_numbers = [i for i in numbers if i <= 0] # genera una lista por cada elemento de la lista numbers que sea negativo o '0'
print(positive_numbers) # [-4, -3, -2, -1, 0]
print('**********************************************')


# Flatten the following list of lists of lists to a one dimensional list
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # matriz
flattened_list = [ number for row in list_of_lists for number in row] # genera una lista de elementos(number) por cada elemento en el fila(row) de la matriz y por cada elemento dentro de la fila
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('**********************************************')


# Using list comprehension create the following list of tuples:
"""
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""
resultado = [tuple([i] + [i**n for n in range(6)]) for i in range(11)] # genera una lista de tuplas de 11 filas de 6 elementos con la estructura inicial del valor de 'i'
print(resultado)
print('****************************************************')


# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries_list = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in countries]
print(countries_list)


# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries_dicctionary = [{'country': country.upper(), 'capital': capital.upper()} for sublist in countries for country, capital in countries]

# Change the following list of lists to a list of concatenated strings:
names = [[('Barbara', 'Liskov')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

names_list = [''.join(tuple) for sublist in names for tuple in sublist]
print(names_list)