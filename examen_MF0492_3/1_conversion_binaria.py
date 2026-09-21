# la función estándar int(texto, 2) para transformar cualquier texto binario en un número entero
def binario_a_decimal_corto(cadena_binaria):
    # Convertimos la cadena directamente a entero indicando la base 2
    resultado = int(cadena_binaria, 2)
    return resultado

# --- Prueba del programa ---
print(binario_a_decimal_corto("1101"))  # Imprime: 13
