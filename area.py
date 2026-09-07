# Calcular el área de un círculo dado su radio
import math
# from math import pi (eficiente)

# Solicitar el radio al usuario
radio = float(input("Introduce el radio del círculo: "))

# Calcular el área (Pi * radio al cuadrado)
area_circulo = math.pi * (radio ** 2)

# Mostrar el resultado
print("El área del círculo es:", area_circulo)
