# Uso de sleep para finalizar
"""
import time

while True:
    
    # get current local time as structured data
    current_time = time.localtime()
    # format the time in 12-hour clock with AM/PM
    formatted_time = time.strftime("%I:%M:%S %p", current_time)
    
    print(formatted_time)
    time.sleep(1)
"""
print('**********************************************')

from datetime import datetime, timedelta

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 10, minute = 35, second = 15)
diff = t2 - t1

# Extraemos los datos válidos de un timedelta
total_dias = diff.days

# Calculamos horas y minutos usando los segundos restantes
horas = diff.seconds // 3600
minutos = (diff.seconds % 3600) // 60
segundos = (diff.seconds % 3600) % 60

# Extraemos y convertimos cada propiedad numérica a binario directamente y descartamos los 2 primeros números del 
# código binario (0b) que genera por defecto el método bin()
dia_bin   = bin(total_dias)[2:]
hora_bin  = bin(horas)[2:]
min_bin   = bin(minutos)[2:]

# Sacamos por pantalla el resultado
print(f"Diferencia real: {total_dias} días, {horas} horas, {minutos} minutos y {segundos} segundos.")
print(f"Día en binario: {dia_bin}")
print(f"Hora en binario: {hora_bin}")
print(f"Minutos en binario: {min_bin}")



"""
Usos de bin() para IoT(programación de microcontroladoras), permisos de seguridad y sistemas de archivos, redes, direcciones IP y MAC,
optimización extrema de espacio(Flags).
"""