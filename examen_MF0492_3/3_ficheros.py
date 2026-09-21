import os
import re
from datetime import datetime

def cuenta_palabras(nombre_archivo):
    # 1. LEER EL ARCHIVO Y CONTAR PALABRAS VALIDAS (En memoria RAM)
    with open(nombre_archivo, 'r', encoding='utf-8') as file:
        contenido = file.read()
        
    # Separamos el texto en un bloque de palabras sueltas
    todas_las_palabras = contenido.split()
    contador_palabras = 0

    for palabra in todas_las_palabras:
        # Excluimos grupos numéricos quitando primero los signos de puntuación (. , ; -) con la expresión regular
        palabra_limpia = re.sub(r'[.,;:_\-¡!¿?()"\']', '', palabra)
        
        # Si después de limpiar el texto NO está vacío y NO es un número, se cuenta
        if palabra_limpia and not palabra_limpia.isdigit():
            contador_palabras += 1

    # 2.CONSTRUIR LA FECHA Y HORA EN ESPAÑOL EXACTO
    ahora = datetime.now()

    # Diccionarios de traducción manual
    dias_semana = {
        0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves",
        4: "Viernes", 5: "Sábado", 6: "Domingo"
    }
    meses_ano = {
        1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio",
        7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
    }

    # Extraemos las piezas del objeto datetime
    nombre_dia = dias_semana[ahora.weekday()]  # .weekday() da un número del 0 al 6
    numero_dia = ahora.day
    nombre_mes = meses_ano[ahora.month]
    ano = ahora.year
    # Formateamos la hora en formato 24 horas usando strftime
    hora_24 = ahora.strftime("%H:%M")

    # Cadena final con la estructura exacta que pide el enunciado
    linea_final = (
        f"\nTotal de palabras válidas: {contador_palabras}. "
        f"Fecha de registro: {nombre_dia}, {numero_dia} de {nombre_mes} de {ano}, a las {hora_24} horas."
    )

    # 3. ESCRIBIR LOS RESULTADOS AL FINAL DEL ARCHIVO (En disco)
    with open(nombre_archivo, 'a', encoding='utf-8') as file:
        file.write(linea_final)

    print("Conteo finalizado. Los datos se han añadido con éxito al final del archivo.")


# INVOCACIÓN Y PRUEBA DE CONSOLA
if __name__ == "__main__":
    # Ruta local de tu examen
    ruta_local = './examen_MF0492_3/ficheros/econom.txt'
    
    # Comprobación de seguridad por si no has creado el archivo lorem para testing
    if not os.path.exists(ruta_local):
        os.makedirs(os.path.dirname(ruta_local), exist_ok=True)
        with open(ruta_local, 'w', encoding='utf-8') as f:
            f.write("Lorem ipsum de prueba 2026. Hoy es un gran día, con 100 o 200 opciones.")

    # Ejecución de la función principal
    cuenta_palabras(ruta_local)
