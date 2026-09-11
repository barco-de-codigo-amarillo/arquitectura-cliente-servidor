# Importamos la función del otro archivo
from procesador import recibir_y_guardar

# Creamos la información que queremos comunicar
info = {
    'Nombre': 'Tadeo',
    'Actividad': 'Dato2',
    'Plataforma': 'Unknown'
}

print('[Principal] Preparando el envío de datos...')

# Enviamos los datos al otro archivo llamando a su función
recibir_y_guardar('extraccion_datos.txt', info)

print('[Principal] Proceso terminado.')