import json

# Implementa una función para solicitar y validar de forma segura 3 números enteros introducidos por el usuario
def obtener_tres_numeros(numero_test):
    lista_numeros = []
    
    # El bucle se repite hasta tener exactamente 3 números válidos
    while len(lista_numeros) < 3:
        numero_actual = len(lista_numeros) + 1
        entrada = input(f"Introduce el número {numero_actual} (0 al 99): ")
        
        try:
            # 1. Intentamos convertir la entrada directamente a número entero
            numero = int(entrada)
            
            # 2. Si la conversión funciona, comprobamos el rango de valores
            if 0 <= numero <= 99:
                # Validamos que no exista ya en la lista
                if numero not in lista_numeros:
                    lista_numeros.append(numero)
                    print(f"-> ¡Número {numero} añadido con éxito!")
                else:
                    print("Error: Ese número ya lo has introducido. No se permiten repeticiones.")
            else:
                print("Error: El número debe estar estrictamente entre 0 y 99.")
                  
        except ValueError:
            # Este bloque se activa SOLO si int() falla (por ejemplo, si el usuario escribe "hola")
            print("Error: Tipo de dato inválido. Debes introducir un número entero.")
            
    return lista_numeros


# Cálculo de faltantes, Intervalos y Excepciones
def calcular_logica_intervalos(numeros_dados):
    """
    Función Modular 2: Cálculo y Excepciones de Negocio.
    Calcula los números faltantes, valida argumentos por tipo/rango
    y mide la amplitud de los 4 intervalos de 0-99.
    """
    # 1. COMPROBACIÓN DE SEGURIDAD (Sin usar raise)
    # Simplemente revisamos con un 'if' si todo está correcto.
    valores_validos = True

    # Validación estricta de excepciones en los argumentos
    for elemento in numeros_dados:
        # Si no es un número entero, o es menor que 0, o es mayor que 99...
        if type(elemento) is not int or elemento < 0 or elemento > 99:
            valores_validos = False
        """
        # raise: para provocar u obligar a que ocurra un error de forma intencionada, detiene un programa cuando ocurre una situación que rompe las reglas del negocio
        if not isinstance(elemento, int) or isinstance(elemento, bool):
            raise TypeError(f"Error en argumento: '{elemento}' no es un número entero.")
        if elemento < 0 or elemento > 99:
            raise ValueError(f"Error en argumento: {elemento} está fuera del rango (0-99).")
        """

    # 2. SI LOS DATOS SON INCORRECTOS, AVISAMOS Y PARAMOS
    if valores_validos == False:
        print("Error en los argumentos: Hay valores inválidos o fuera de rango (0-99).")
        return # El return vacío detiene la función limpiamente sin romper el programa

    # 3. SE EJECUTA LA LÓGICA NORMAL EN AUSENCIA DE DATOS INVÁLIDOS
    # Definimos el mínimo y máximo de la lista
    minimo = min(numeros_dados)
    maximo = max(numeros_dados)

    # Encontrar números faltantes intermedios
    faltantes = []
    for num in range(minimo + 1, maximo):
        if num not in numeros_dados:
            faltantes.append(num)

    # Ordenación de los puntos de corte e imposibilidad de duplicados
    cortes = sorted(list(set(numeros_dados)))
    while len(cortes) < 3:
        cortes.append(cortes[-1]) # Relleno por seguridad si hay repetidos

    # Desempaqueta la lista
    n1, n2, n3 = cortes

    # Diccionario dinámico con el conteo inclusivo (+1) de cada tramo
    diccionario_intervalos = {
        "intervalo_1_amplitud": n1,
        "intervalo_2_amplitud": n2 - n1,
        "intervalo_3_amplitud": n3 - n2,
        "intervalo_4_amplitud": 99 - n3
    }

    return faltantes, diccionario_intervalos


# =====================================================================
# INVOCACIÓN Y DOS PRUEBAS DE TEST DE USUARIO COMPLETAS EN CONSOLA
# =====================================================================
if __name__ == "__main__":
    print("=== INICIANDO SCRIPT DE VERIFICACIÓN ===")

    # -----------------------------------------------------------------
    # EJECUCIÓN 1: TEST DE USUARIO 1
    # -----------------------------------------------------------------
    datos_test_1 = obtener_tres_numeros(numero_test=1)
    
    try:
        faltantes_1, diccionario_1 = calcular_logica_intervalos(datos_test_1)
        
        # REQUISITO: Transformar dicho diccionario a formato JSON sin función externa
        json_resultado_1 = json.dumps(diccionario_1, indent=4, ensure_ascii=False)
        
        # Visualización de Resultados 1
        print(f"\nRESULTADOS TEST 1:")
        print(f"Lista de números que faltan intermedios: {faltantes_1}")
        print("Diccionario transformado a Formato JSON:")
        print(json_resultado_1)
        
    except (TypeError, ValueError) as e:
        print(f"Excepción controlada en Test 1: {e}")

    print("\n" + "="*60 + "\n")

    # -----------------------------------------------------------------
    # EJECUCIÓN 2: TEST DE USUARIO 2 (Para comprobar dinamismo)
    # -----------------------------------------------------------------
    datos_test_2 = obtener_tres_numeros(numero_test=2)
    
    try:
        faltantes_2, diccionario_2 = calcular_logica_intervalos(datos_test_2)
        
        # REQUISITO: Transformar dicho diccionario a formato JSON sin función externa
        json_resultado_2 = json.dumps(diccionario_2, indent=4, ensure_ascii=False)
        
        # Visualización de Resultados 2
        print(f"\nRESULTADOS TEST 2:")
        print(f"Lista de números que faltan intermedios: {faltantes_2}")
        print("Diccionario transformado a Formato JSON:")
        print(json_resultado_2)
        
    except (TypeError, ValueError) as e:
        print(f"Excepción controlada en Test 2: {e}")

    print("\n=== FIN DE LAS PRUEBAS EN CONSOLA ===")