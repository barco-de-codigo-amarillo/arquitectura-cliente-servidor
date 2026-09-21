import requests
from bs4 import BeautifulSoup
#url = 'https://archive.ics.uci.edu/ml/datasets.php'
# URL de Worldometer en español
url = "https://www.worldometers.info/es/poblacion-mundial/poblacion-por-pais/"

# Añadimos un User-Agent para simular una petición desde el navegador y evitar bloqueos
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
try:
    # Realizar la petición HTTP
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Lanza un error si la descarga falla
    
    # Parsear el HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Localizar la tabla por su ID común en Worldometer ('example2')
    # Si cambia, se puede buscar simplemente la etiqueta <table>
    tabla = soup.find('table', id='example2') or soup.find('table')
    
    if tabla:
        # Buscar todas las filas de la tabla
        filas = tabla.find('tbody').find_all('tr')
        
        datos_india = []
        for fila in filas:
            # Obtener las celdas de cada fila
            celdas = fila.find_all('td')
            
            # Verificar si la fila tiene datos y si corresponde a 'India'
            if celdas and "India" in celdas[1].text:
                # Extraemos el texto limpio de cada celda de la fila de la India
                datos_india = [celda.text.strip() for celda in celdas]
                break
        
        if datos_india:
            # Estructurar e imprimir los resultados de forma legible
            columnas = [
                "Posición", "País", "Población", "Cambio anual", "Cambio neto", 
                "Densidad (Hab/Km²)", "Superficie (Km²)", "Migrantes (neto)", 
                "Tasa Fec.", "Edad mediana", "% Población Urbana", "Cuota Mundial"
            ]
            
            print("=== DATOS EXTRAÍDOS DE LA INDIA ===")
            for i, valor in enumerate(datos_india):
                # Evitar desajustes si cambian el número de columnas de la web
                if i < len(columnas):
                    print(f"{columnas[i]}: {valor}")
        else:
            print("No se encontraron los datos específicos de la India en la tabla.")
    else:
        print("No se pudo localizar la tabla de datos en la página web.")

except requests.exceptions.RequestException as e:
    print(f"Error al realizar la petición: {e}")

# Con los datos para Brasil construir un titular que diga "Brasil" ha alcanzado una población de XXXX con una densidad de YYYY y con una porcentaje de población urbana del ZZZZ