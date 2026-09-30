from datetime import datetime
import requests
from bs4 import BeautifulSoup
from seismo import generar_reporte

# =====================================================================
# CLASE CONSTRUCTORA POO
# =====================================================================
class RegistroSeismo:
    def __init__(self, fecha_hora: datetime, ubicacion: str, magnitud: float):
        self.fecha_hora = fecha_hora
        self.ubicacion = ubicacion
        self.magnitud = magnitud

    def generar_reporte(self) -> str:
        fecha_formateada = f"{self.fecha_hora.day}/{self.fecha_hora.month}/{self.fecha_hora.strftime('%y')}"
        hora_formateada = self.fecha_hora.strftime("%H:%M:%S")
        return f"A las {hora_formateada} del {fecha_formateada} hubo un seísmo de magnitud {self.magnitud:.1f} en {self.ubicacion}"


# =====================================================================
# CAPTACIÓN, EXTRACCIÓN CORREGIDA Y CONSTRUCCIÓN
# =====================================================================

url = "https://www.ign.es/web/ign/portal/ultimos-terremotos/-/ultimos-terremotos/get30dias"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Brave/120"
}

response = requests.get(url, headers=headers)
lista_diccionarios_final = []

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Busca todas las filas 'tr' de la tabla
    filas = soup.find_all('tr')
    
    for fila in filas:
        celdas = fila.find_all('td')
        
        # Valida que la fila contenga las columnas de datos (mínimo 12)
        if len(celdas) >= 12:
            try:
                # Saca el texto limpio de cada celda por su índice
                evento_id = celdas[0].get_text(strip=True)      
                fecha_str = celdas[1].get_text(strip=True)      
                hora_str = celdas[2].get_text(strip=True)       
                magnitud_str = celdas[7].get_text(strip=True)   
                localizacion = celdas[10].get_text(strip=True)  

                # Filtro de seguridad: Omite si es la línea de cabeceras o si la fila está vacía
                if "Fecha" in fecha_str or not evento_id.startswith("es"):
                    continue

                # CONSTRUCCIÓN
                # Pasa el string a tipo datetime y float de Python
                fecha_hora_utc = datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M:%S")
                magnitud = float(magnitud_str)
                
                # Guarda la relación clave-valor pura sin formato JSON
                seismo_dict = {
                    "Localización(str)": localizacion,
                    "fecha y hora UTC (datetime)": fecha_hora_utc,
                    "magnitud(float)": magnitud
                }
                
                lista_diccionarios_final.append(seismo_dict)
                
            except (ValueError, IndexError):
                # Si una fila da error en los índices o conversión, pasa a la siguiente
                continue

# =====================================================================
# SALIDA POR TERMINAL DE LA LISTA DE DICCIONARIOS
# =====================================================================
print(f"Status Code: {response.status_code}")
print(f"Total registros en la lista de diccionarios: {len(lista_diccionarios_final)}\n")

print("LISTADO EN FORMATO LISTA DE DICCIONARIOS:")
print(lista_diccionarios_final)
print("-" * 90)

# Prueba de instanciación con el primer diccionario de la lista
if lista_diccionarios_final:
    sismo_muestra = lista_diccionarios_final[0]
    
    objeto_prueba = RegistroSeismo(
        fecha_hora=sismo_muestra["fecha y hora UTC (datetime)"],
        ubicacion=sismo_muestra["Localización(str)"],
        magnitud=sismo_muestra["magnitud(float)"]
    )
    
    print("PROBANDO LA INSTANCIACIÓN Y EL MÉTODO DE TU CLASE:")
    print(f"**{objeto_prueba.generar_reporte()}**")
