def recibir_y_guardar(nombre_archivo, datos):
    """ Recibe datos de otro archivo y los vuelca en un txt """
    print(f"[Procesador] Recibiendo datos para {nombre_archivo}...")

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for clave, valor in datos.items():
            archivo.write(f'{clave} : {valor}\n')

    print(f"[Procesador] Datos guardados.")