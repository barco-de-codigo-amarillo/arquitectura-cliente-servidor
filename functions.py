# Arbitrary Number of Named Arguments
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)
print('***********************************************************')

# Returning a list
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
print('***********************************************************')


# Function with Default Parameters
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Amarillo'))
print('***********************************************************')

def generate_full_name (first_name = 'Amarillo', last_name = 'Barco'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))
print('***********************************************************')

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age 
print('Age: ', calculate_age(1821))
print('***********************************************************')

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
print('***********************************************************')


# Función con argumento de valor fijo, argumento con valor opcional y argumento con cantidad de longitud variable
def registrar_estudiante(nombre, beca=None, *calificaciones):
    print(f"Estudiante: {nombre}")
    
    # Comprobamos el valor de None
    if beca is None:
        print("Estado de beca: No aplica / Sin información")
    else:
        print(f"Estado de beca: {beca}")
    
    # Procesamos los argumentos de longitud variable
    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"Calificaciones recibidas: {calificaciones} | Promedio: {promedio}")
    else:
        print("Calificaciones recibidas: Ninguna registrada")
    print("-" * 30)

# --- EJEMPLOS DE CÓMO LLAMAR A LA FUNCIÓN ---

# Ejemplo 1: Pasando todos los datos (el argumento variable recibe 3 notas)
registrar_estudiante("Carlos", "Beca Completa", 8, 9, 10)

# Ejemplo 2: Dejando la beca en None y pasando 2 notas
registrar_estudiante("Ana", None, 7, 8)

# Ejemplo 3: Solo pasando el argumento fijo (beca es None y notas queda vacío)
registrar_estudiante("Luis")
print('***********************************************************')

# Llamando a otras funciones
def elevarlo_a_si_mismo(n):
    return n**n

def calcular(f, x):
    return f(x)

print(calcular(elevarlo_a_si_mismo, 3))