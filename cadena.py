# Slicing de cadenas

language = 'Python'
first_three = language[0:3] # empieza en índice 0, hasta 3 pero sin incluir 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Otra forma
last_three = language[-3:] # son las últimas tres letras desde el final
print(last_three)   # hon
last_three = language[3:] # 
print(last_three)   # hon


# Invertir cadenas

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH


# Saltar caracteres al hacer slicing

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto