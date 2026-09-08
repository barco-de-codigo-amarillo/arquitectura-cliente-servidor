# syntax
"""
if condition:
    code
elif condition:
    code
else:
    code
"""

# Comprobación de signo de un número
a = int(input('Enter a number: '))
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')


# Comprobación de paridad y signo de un número
b = int(input('Enter a number: '))

if b % 2 == 0:
    print('B is an even number')
else:
    print('B is an odd number')
    b = int(b)
if b > 0:
    print('B is a positive number')
elif b < 0:
    print('B is a negative number')
else:
    print('B is zero')


# Comprobación de tipos
c = input('Enter a number: ')
if type(c) == int:
    print(f'{c} is an integer')
elif type(c) == float:
    print(f'{c} is a float number')
elif type(c) is str:
    print(f'{c} is a string')
elif c.isdecimal() == True:
    print(f'{c} is a decimal number')
elif c.isdigit() == True:
    print(f'{c} is a digit number')
elif c.isnumeric() == True:
    print(f'{c} is a numeric number')