# Exception
try:
    entrada = int(input('Introduce un número: '))
    print('Aquí es correcto')
except Exception as e: # captura la excepción
    print(f'Aquí es excepción: {e}')
finally:
    print('I always run. Here code that kill process')


# ValueError
try:
    entrada = int(input('Introduce un número: '))
    print('Aquí es correcto')
except ValueError: # queremos trabajar con ValueError por ello forzamos el casting de 'int'
    print('Aquí es excepción')
finally:
    print('I always run. Here code that kill process')


# Complete structure
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block') # se ejecuta cuando no hay excepción
finally:
    print('I alway run.')

