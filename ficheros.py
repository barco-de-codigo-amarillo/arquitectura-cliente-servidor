# Abre por defecto en modo lectura
# f = open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

"""
"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

"""
read(): read the whole text as string. If we want to limit the number of characters 
we want to read, we can limit it by passing int value to the read(number) method.
"""
f = open('./files/lorem.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

# print the first 10 characters of the text file
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

"""
readline(): read only the first line
"""
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

"""
readlines(): read all the text line by line and returns a list of lines
"""
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# Another way to get all the lines as a list is using splitlines():
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

"""
After we open a file, we should close it. There is a new way of opening files using with - closes the files by itself.
"""

with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)


"""
Opening Files for Writing and Updating
"a" - append - will append to the end of the file, if the file does not exist it creates a new file.
"w" - write - will overwrite any existing content, if the file does not exist it creates
"""
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')


"""
Deleting files
"""

import os
os.remove('./files/example.txt')


# If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:

import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')


"""
File types
"""
# JSON
countries_list = '''[
    {
        "name": "Estonia",
        "capital": "Tallinn",
        "languages": ["Estonian"],
        "population": 1300000,
        "is_island": False
    },
    {
        "name": "Finland",
        "capital": "Helsinki",
        "languages": ["Finnish", "Swedish"],
        "population": 5500000,
        "is_island": False
    },
    {
        "name": "Iceland",
        "capital": "Reykjavík",
        "languages": ["Icelandic"],
        "population": 390000,
        "is_island": True
    }
]'''

# let's change JSON to dictionary
import json
countries_dct_I = json.loads(countries_list)
print(type(countries_dct_I))
print(countries_dct_I)
print(countries_dct_I['name'])

# Dictionary
countries_dct_II = {
        "name": "Finland",
        "capital": "Helsinki",
        "languages": ["Finnish", "Swedish"],
        "population": 5500000,
        "is_island": False
    }


# Changing Dictionary to JSON
import json
# let's convert it to  json
countries_json = json.dumps(countries_dct_II, indent=4) # El número representa la cantidad de espacios en blanco que se colocarán en cada nivel de profundidad (sangría); estándar en la industria es usar indent=4 o indent=2; indent=0, solo pondrá saltos de línea
print(type(countries_json))
print(countries_json)

# Saving as JSON File
with open('./files/json_example.json', 'w', encoding='utf-8') as f: # encoding=utf-8 traduce los bytes correctos en el DISCO
    json.dump(countries_dct_II, f, ensure_ascii=False, indent=4) # ensure-ascii=False mantiene los caracteres reales en texto en la RAM


"""
Punteros: .seek(n)
"""
with open("json_example.json", "r", encoding="utf-8") as archivo:
    # 1. Leemos todo el contenido por primera vez
    primer_intento = archivo.read()
    print("--- Primera Lectura ---")
    print(primer_intento) # Muestra el texto perfectamente
    
    # Si intentamos leer aquí de nuevo:
    segundo_intento = archivo.read()
    print("--- Segunda Lectura ---")
    print(segundo_intento) # ¡IMPRIME VACÍO! El cursor está al final del archivo.

    #  SOLUCIÓN: Movemos el cursor al byte 0 (el inicio)
    archivo.seek(0)
    
    # 3. Ahora sí podemos volver a leerlo
    tercer_intento = archivo.read()
    print("--- Tercera Lectura (Tras hacer .seek) ---")
    print(tercer_intento) # Vuelve a mostrar todo el texto


"""
.insert() — Para Listas (En memoria): 
añade un elemento en una posición (índice) específica de una lista, 
empujando los elementos existentes hacia la derecha 
"""

paises = ["Estonia", "Finland", "Norway"]

# Queremos meter "Sweden" en la posición 1 (el segundo lugar)
paises.insert(1, "Sweden")

print(paises)
# Salida: ['Estonia', 'Sweden', 'Finland', 'Norway']


"""
.writelines() - Para Archivos (En disco):
escribir una lista de cadenas de texto (strings) de golpe dentro 
de un archivo.
No añade saltos de línea de forma automática, si no le pones un \n al final de cada texto en tu lista,
escribirá todo pegado en una sola línea continua.
Cuando ejecutas insert(), Python modifica los unos y ceros directamente dentro de tu memoria RAM. Es 
instantáneo. Sin embargo, el archivo físico en tu disco duro no ha cambiado en absoluto. Si el 
programa termina en la siguiente línea o la luz se corta, ese cambio se pierde para siempre.

Modificar datos en la memoria RAM es miles de veces más rápido que escribir en el disco duro. Por 
eso, la buena práctica en Python es:Leer el archivo y pasarlo a la memoria RAM (readlines()).Hacer
todas las modificaciones pesadas en la memoria con métodos rápidos como insert(), append(), map() 
o filter().Una vez que todo está perfecto, hacer un único viaje al disco para guardarlo para siempre
(writelines() o json.dump()).
"""

lineas_texto = [
    "Primera línea del archivo.\n",
    "Segunda línea del archivo.\n",
    "Tercera línea del archivo.\n"
]

# Abrimos el archivo en modo 'w' (escritura)
with open("mi_archivo.txt", "w", encoding="utf-8") as archivo:
    # Escribe toda la lista de strings de una sola vez
    archivo.writelines(lineas_texto)

print("¡Archivo escrito con éxito!")


"""
Conversión de objeto json para manejo como fichero
"""

import json
import io

# 1. Tenemos un objeto nativo de Python (diccionario)
objeto_pais = {
    "name": "Estonia",
    "capital": "Tallinn",
    "population": 1300000
}

# 2. Lo transformamos a una cadena de texto en formato JSON
texto_json = json.dumps(objeto_pais, indent=4)

# 3. ¡AQUÍ ESTÁ EL TRUCO!: Convertimos el texto en un "fichero virtual"
fichero_virtual = io.StringIO(texto_json)

# --- A partir de aquí, 'fichero_virtual' se maneja como un fichero real ---

# Podemos leerlo usando métodos de ficheros tradicionales
print("--- Leyendo desde el fichero virtual ---")
contenido = fichero_virtual.read()
print(contenido)

# Al igual que vimos antes, el cursor se queda al final tras la lectura.
# Si queremos volver a usarlo, aplicamos el rebobinado de cursor:
fichero_virtual.seek(0)

# Al comportarse como un fichero, se lo podemos pasar directamente a json.load()
# (que normalmente solo acepta ficheros físicos creados con open())
datos_decodificados = json.load(fichero_virtual)
print("\n--- Comprobación de que vuelve a ser un objeto ejecutable ---")
print(f"La capital de {datos_decodificados['name']} es {datos_decodificados['capital']}")

# Cerramos el fichero virtual para liberar el espacio de la memoria RAM
fichero_virtual.close()


"""
csv - Comma-Separated Values o Valores Separados por Comas
es el formato estándar y más sencillo de la informática para
almacenar datos en forma de tabla (filas y columnas) utilizando
texto plano.
Puente universal entre los archivos de texto y programas de
hojas de cálculo como Excel o bases de datos relacionales
"""
import csv

# 1. Datos que queremos guardar (Lista de listas)
datos_paises = [
    ["name", "capital", "population", "is_island"], # Cabecera
    ["Estonia", "Tallinn", 1300000, False],
    ["Finland", "Helsinki", 5500000, False],
    ["Iceland", "Reykjavík", 390000, True]
]

# ==========================================
# FASE 1: ESCRIBIR UN ARCHIVO CSV
# ==========================================
# 'newline=""' evita que Python agregue líneas en blanco dobles en Windows
with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    # Escribimos todas las filas de golpe
    escritor.writerows(datos_paises)

print("Archivo 'paises.csv' creado con éxito.")


# ==========================================
# FASE 2: LEER EL ARCHIVO CSV
# ==========================================
with open("paises.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    
    print("\n--- CONTENIDO DEL CSV PROCESADO ---")
    for fila in lector:
        # 'fila' es una lista de Python automática: ['Estonia', 'Tallinn', '1300000', 'False']
        print(f"País: {fila[0]} | Capital: {fila[1]} | Población: {fila[2]}")



# Manejo de un archivo csv externo
# ejemplo I:
import csv

# Leemos directamente desde el archivo externo que creamos en el Paso 1
with open("csv_example.csv", "r", encoding="utf-8") as archivo:
    # Usamos DictReader para que asocie automáticamente cada dato con su cabecera (columna)
    lector_diccionario = csv.DictReader(archivo)
    
    print("--- LEYENDO DATOS DEL ARCHIVO CSV EXTERNO ---")
    for fila in lector_diccionario:
        # Ahora 'fila' es un diccionario inteligente: {'name': 'Estonia', ...}
        print(f"País: {fila['name']} | Capital: {fila['capital']} | Población: {int(fila['population']):,}")


# ejemplo II:
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')