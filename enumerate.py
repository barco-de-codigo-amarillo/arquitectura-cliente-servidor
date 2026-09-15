# Creación de ranking o lista enumerada
consolas = ['PlayStation 5', 'Nintendo Switch', 'Xbox Series X']



# Indicamos el ", 1" para que empiece a contar desde el uno en lugar del cero
for indice, consola in enumerate(consolas, 1):
    print(f"Puesto {indice}: {consola}")


# Modificar datos de una lista
precios = [10, 50, 100, 200]

# Queremos aplicar un 10% de descuento a cada precio de la lista
for indice, precio in enumerate(precios):
    precios[indice] = precio * 0.90

print(precios)
# Salida: [9.0, 45.0, 90.0, 180.0]



# Filtrar elementos
datos_usuarios = [
    ['Nombre', 'Edad'],  # Cabecera (Índice 0)
    ['Ana', 25],         # Datos (Índice 1)
    ['Carlos', 30]       # Datos (Índice 2)
]

for indice, fila in enumerate(datos_usuarios):
    if indice == 0:
        continue  # Nos saltamos la cabecera
    print(f"Procesando a: {fila[0]} ({fila[1]} años)")
