# extractor.py
from datetime import datetime
import json
import requests
from bs4 import BeautifulSoup

# IMPORTACIÓN MODULAR: Importamos la clase Sismo desde tu archivo seismo.py
from seismo import Sismo

# =====================================================================
# 1. CAPTACIÓN, EXTRACCIÓN Y CONSTRUCCIÓN DE LA LISTA
# =====================================================================
url = "https://www.ign.es/web/ign/portal/ultimos-terremotos/-/ultimos-terremotos/get30dias"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Brave/120"
}

response = requests.get(url, headers=headers)
lista_diccionarios_final = []

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    filas = soup.find_all('tr')
    
    for fila in filas:
        celdas = fila.find_all('td')
        if len(celdas) >= 12:
            try:
                evento_id = celdas[0].get_text(strip=True)      
                fecha_str = celdas[1].get_text(strip=True)      
                hora_str = celdas[2].get_text(strip=True)       
                magnitud_str = celdas[7].get_text(strip=True)   
                localizacion = celdas[10].get_text(strip=True)  

                if "Fecha" in fecha_str or not evento_id.startswith("es"):
                    continue

                fecha_hora_utc = datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M:%S")
                magnitud = float(magnitud_str)
                
                seismo_dict = {
                    "Localización(str)": localizacion,
                    "fecha y hora UTC (datetime)": fecha_hora_utc,
                    "magnitud(float)": magnitud
                }
                lista_diccionarios_final.append(seismo_dict)
                
            except (ValueError, IndexError):
                continue

# =====================================================================
# 2. CREACIÓN DE LA REPRESENTACIÓN JSON
# =====================================================================
json_resultado = json.dumps(
    lista_diccionarios_final,
    indent=4,
    ensure_ascii=False,
    default=lambda obj: obj.strftime("%Y-%m-%d %H:%M:%S") if isinstance(obj, datetime) else obj
)


# =====================================================================
# 3. CONSTRUCCIÓN DEL OBJETO 'SISMO' DESDE LA DATA EXTRAÍDA
# =====================================================================
if __name__ == "__main__":
    print("--- REPRESENTACIÓN JSON GENERADA (Muestra de la estructura) ---")
    # Mostramos un fragmento del JSON puro para verificar su creación
    print(json_resultado[:350] + "\n...\n]")
    print("-" * 90)

    if lista_diccionarios_final:
        print("--- CREACIÓN DEL OBJETO DESDE LA DATA ---")
        
        # OPCIÓN A: Crear el objeto directamente desde el primer diccionario de la lista
        primer_diccionario = lista_diccionarios_final[0]
        
        objeto_desde_dict = Sismo(
            fecha_hora=primer_diccionario["fecha y hora UTC (datetime)"],
            ubicacion=primer_diccionario["Localización(str)"],
            magnitud=primer_diccionario["magnitud(float)"]
        )
        
        # OPCIÓN B: Crear el objeto reconstruyendo la información desde la representación JSON string
        datos_desde_json = json.loads(json_resultado)
        primer_item_json = datos_desde_json[0]
        
        # Al venir del JSON, la fecha es un string, por lo que la parseamos de vuelta a datetime
        fecha_objeto = datetime.strptime(primer_item_json["fecha y hora UTC (datetime)"], "%Y-%m-%d %H:%M:%S")
        
        objeto_desde_json = Sismo(
            fecha_hora=fecha_objeto,
            ubicacion=primer_item_json["Localización(str)"],
            magnitud=primer_item_json["magnitud(float)"]
        )
        
        # Ejecución y visualización de reportes de los objetos creados dinámicamente
        print("Reporte del Objeto instanciado desde el Diccionario:")
        print(f"**{objeto_desde_dict.generar_reporte()}.")
        
        print("\nReporte del Objeto instanciado desde el String JSON decodificado:")
        print(f"**{objeto_desde_json.generar_reporte()}.")
        print("-" * 90)
