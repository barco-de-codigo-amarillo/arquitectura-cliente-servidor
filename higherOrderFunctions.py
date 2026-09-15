# Function as a parameter
def sum_numbers(nums):  # normal function
    return sum(nums) 

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
print('****************************************************')


# Function as a return value
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
print('****************************************************')


# Python clousures
def add_ten():
    ten = 10
    def add(num): # espera recibir un número
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
print('****************************************************')


# Python Decorator
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
print('****************************************************')


'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Barbara", "Liskov",'California')

# Python - Map function
# the map() function is a built-in function that takes a function and iterable as parameters
# Transforms every item in the iterable using a formula.Same size as the original list.
numbers = [1, 2, 3, 4, 5] # iterable
def square(x): # function
    return x ** 2
numbers_squared = map(square, numbers) # map(function, list=iterable)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]


# Python - Filter functions 
# Lets filter only even nubers
# Extracts items that meet a specific True/False condition.Smaller or equal size.
"""
The filter() function calls the specified function which returns boolean for each item of
the specified iterable (list). It filters the items that satisfy the filtering criteria.
"""
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num): # function
    if num % 2 == 0: # si es par
        return True
    return False

even_numbers = filter(is_even, numbers) # filter(function, iterable)
print(list(even_numbers))       # [2, 4]


# Python - ReduceFunction
# Combines all items into a single final value (e.g., a sum).One single value (not a list).
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)


from functools import reduce # Importación obligatoria

total = reduce(add_two_nums, numbers_str)
print(total)    # 15

