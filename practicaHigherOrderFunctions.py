"""
LEVEL 1
"""

# Differences between Map, Filter y Reduce

# Map: transforms to a data collection
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))

print(squared)  # Output: [1, 4, 9, 16]

# Filter: filter with a condition True/False
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)  # Output: [2, 4, 6]


# Reduce: combines all the items that find into a list or other iterable element, the result is a single value
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 24  -> (((1 * 2) * 3) * 4)


# The difference between higher order function, closure and decorator

# Higher order functions:  Accepts or returns other functions.
def execute_twice(func, value):
    return func(func(value))

add_five = lambda x: x + 5
print(execute_twice(add_five, 10)) # Output: 20 (10 + 5 + 5)


# Closure: Remembers environmental data from an outer functions.
def make_multiplier(x):
    # 'x' is a local variable of the outer function
    def multiplier(n):
        return x * n # The inner function remembers 'x'
    return multiplier

double = make_multiplier(2) 
# The 'make_multiplier' function has finished executing here!
# But 'double' still remembers that x was 2.

print(double(5)) # Output: 10


# Decorator: Extends or modifies a function's behavior dynamically.
# 1. We create the decorator (It's a Higher-Order Function + Closure)
def my_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Executing function: {func.__name__}")
        result = func(*args, **kwargs)
        print("Execution finished!")
        return result
    return wrapper

# 2. We apply it using the @ symbol
@my_logger
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")
# Output:
# Executing function: greet
# Hello, Alex!
# Execution finished!


# Use filter to filter out countries containing 'land'.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

countries_with_land = list(filter(lambda c: 'land' in c.lower(), countries))

print(countries_with_land) # ['Finland', 'Iceland']


# Use filter to filter out countries having exactly six characters.
countries_list_6_characters = list(filter(lambda word: len(word) == 6, countries))

print(countries_list_6_characters)
print('***********************************************')

# Use filter to filter out countries containing six letters and more in the country list.
countries_list_with_filter = list(filter(lambda word: len(word) >= 6, countries))

print(countries_list_with_filter)
print('***********************************************')

# Use filter to filter out countries starting with an 'E'
countriesStartsWith = [c for c in countries if c.lower().startswith('e')]

print(countriesStartsWith)
print('***********************************************')

# Use filter to filter out countries starting with an 'E'
countries_with_E = list(filter(lambda word: 'E' in word.upper(), countries))

print(countries_with_E)
print('***********************************************')


# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

numbers = [2, 5, 8, 3, 10]

# 1. map duplica -> 2. filter limpia -> 3. reduce suma todo
total = reduce(lambda x, y: x + y, filter(lambda x: x > 10, map(lambda x: x * 2, numbers)))

print(total) # Output: 36 (16 + 20)
print('***********************************************')

"""
LEVEL 2
"""
# Use map to create a new list by changing each country to uppercase in the countries list
countries_upper = list(map(lambda c: c.upper(), countries))
print(countries_upper)
print('***********************************************')

# Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_list = list(map(lambda n: n ** 2, numbers))
print(numbers_list)
print('***********************************************')

# Use map to change each name to uppercase in the names list
names = ['Barbara', 'David', 'Bjarne', 'Linus']
names_list = list(map(lambda name: name.upper(), names))
print(names_list)
print('***********************************************')


# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items
def get_string_lists(lst):
    lst_str = list(filter(lambda isStr: type(isStr) == str, lst))
    return lst_str

print(get_string_lists(names))
print('***********************************************')


# Use reduce to sum all the numbers in the numbers list
from functools import reduce
numbers_with_reduce = reduce(lambda x, y: x + y, numbers)

print(numbers_with_reduce)
print('***********************************************')


# Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# 1. Usamos reduce para unir los países uno a uno
def concatenar_paises(acumulado, siguiente):
    # Si el siguiente país es el último de la lista, le ponemos ", and " antes
    if siguiente == countries[-1]:
        return f"{acumulado}, and {siguiente}"
    # Para todos los demás países, los unimos con una coma y espacio
    return f"{acumulado}, {siguiente}"

# 2. Aplicamos reduce con nuestra función
lista_concatenada = reduce(concatenar_paises, countries)

# 3. Formamos la frase final metiendo el resultado en el string
frase_final = f"{lista_concatenada} are north European countries"

print(frase_final)
print('***********************************************')


# Create a function returning a dictionary, where keys stand for starting letters of 
# countries and values are the number of country names starting with that letter.
def count_starting_letters(country_list):
    # 1. Creamos el diccionario vacío donde guardaremos los conteos
    letter_counts = {}
    
    # 2. Recorremos cada país de la lista
    for country in country_list:
        # Extraemos la primera letra en mayúscula
        first_letter = country[0].upper()
        
        # 3. Si la letra ya existe en el diccionario, sumamos 1 al contador
        if first_letter in letter_counts:
            letter_counts[first_letter] += 1
        # Si es la primera vez que vemos la letra, la inicializamos en 1
        else:
            letter_counts[first_letter] = 1
            
    return letter_counts

# Ejecutamos la función pasándole nuestra lista de países
print(count_starting_letters(countries))
print('***********************************************')

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder
# 1. Agregamos la ruta o importamos directamente la lista desde la carpeta data
import sys
sys.path.append("data")  # Le dice a Python que busque dentro de la carpeta 'data'
from countries import countries  # Importa la lista de países

# 2. Declaramos la función solicitada
def get_first_ten_countries(country_list):
    # Usamos slicing [:10] para obtener los elementos desde el índice 0 hasta el 9
    return country_list[:10]

# 3. Probamos la función imprimiendo el resultado
first_ten = get_first_ten_countries(countries)
print(first_ten)
print('***********************************************')


# Declare a get_last_ten_countries function that returns the last ten countries in the countries list
import sys
sys.path.append("data")  # Asegura que Python encuentre la carpeta data
from countries import countries  # Importa la lista original de países

# Declaramos la función para obtener los últimos 10
def get_last_ten_countries(country_list):
    # El índice -10 indica que empiece 10 posiciones antes del final
    # Al dejar vacío el espacio después de los dos puntos, va hasta el último elemento
    return country_list[-10:]

# Probamos la función
last_ten = get_last_ten_countries(countries)
print(last_ten)
print('***********************************************')


# Use the countries_data.py to:
import sys
sys.path.append("data")  # Asegura que Python encuentre la carpeta data
from countries_data import countries_data  # Importa la lista original de países

# Sort countries by name, by capital, by population.
# 1. Ordenar por NOMBRE (Alfabético A-Z)
by_name = sorted(countries_data, key=lambda c: c["name"])

# 2. Ordenar por CAPITAL (Alfabético A-Z)
by_capital = sorted(countries_data, key=lambda c: c["capital"])

# 3. Ordenar por POBLACIÓN (De Mayor a Menor)
# Usamos reverse=True para que los números vayan descendentes
by_population = sorted(countries_data, key=lambda c: c["population"], reverse=True)

# --- PRUEBAS DE IMPRESIÓN ---
print("--- ORDENADO POR NOMBRE ---")
for c in by_name: print(c)
print('***********************************************')

print("\n--- ORDENADO POR POBLACIÓN (MAYOR A MENOR) ---")
for c in by_population: print(c)
print('***********************************************')


# Sort out the ten most spoken languages by location.
# 1. Importamos los datos (asegúrate de tener el archivo countries_data en tu carpeta)
import sys
sys.path.append("data")
from countries_data import countries_data

def most_spoken_languages(data, limit=10):
    language_counts = {}
    
    # 2. Recorremos cada país y cada uno de sus idiomas
    for country in data:
        for language in country["languages"]:
            # Si el idioma ya está, sumamos 1 país (ubicación)
            if language in language_counts:
                language_counts[language] += 1
            # Si no está, lo inicializamos en 1
            else:
                language_counts[language] = 1
                
    # 3. Ordenamos el diccionario por sus valores (conteos) de mayor a menor
    sorted_languages = sorted(
        language_counts.items(), 
        key=lambda item: item[1], 
        reverse=True
    )
    
    # 4. Devolvemos únicamente los primeros 10
    return sorted_languages[:limit]

# Ejecutamos e imprimimos el resultado de los 10 más hablados
ten_most_spoken = most_spoken_languages(countries_data, 10)

print("--- TEN MOST SPOKEN LANGUAGES BY LOCATION ---")
for rank, (lang, count) in enumerate(ten_most_spoken, 1):
    print(f"{rank}. {lang}: spoken in {count} countries")


# Sort out the ten most populated countries.
# 1. Importamos los datos (asegúrate de tener el archivo countries_data en tu carpeta)
import sys
sys.path.append("data")
from countries_data import countries_data

def most_spoken_languages(data, limit=10):
    language_counts = {}
    
    # 2. Recorremos cada país y cada uno de sus idiomas
    for country in data:
        for language in country["languages"]:
            # Si el idioma ya está, sumamos 1 país (ubicación)
            if language in language_counts:
                language_counts[language] += 1
            # Si no está, lo inicializamos en 1
            else:
                language_counts[language] = 1
                
    # 3. Ordenamos el diccionario por sus valores (conteos) de mayor a menor
    sorted_languages = sorted(
        language_counts.items(), 
        key=lambda item: item[1], 
        reverse=True
    )
    
    # 4. Devolvemos únicamente los primeros 10
    return sorted_languages[:limit]

# Ejecutamos e imprimimos el resultado de los 10 más hablados
ten_most_spoken = most_spoken_languages(countries_data, 10)

print("--- TEN MOST SPOKEN LANGUAGES BY LOCATION ---")
for rank, (lang, count) in enumerate(ten_most_spoken, 1):
    print(f"{rank}. {lang}: spoken in {count} countries")