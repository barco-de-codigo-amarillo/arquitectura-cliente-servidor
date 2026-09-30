# api.py
from fastapi import FastAPI, status
import uvicorn

# IMPORTACIONES MODULARES: Traemos la clase y la lista extraída de tus otros archivos
from seismo import Sismo
from extractor import lista_diccionarios_final

# Inicializamos la aplicación FastAPI
app = FastAPI(
    title="API REST Sismológica - IGN",
    description="Servicio backend modular para el filtrado y consulta de eventos sísmicos.",
    version="1.0.0"
)

# =====================================================================
# ENDPOINT GET: SISMOS CON MAGNITUD >= 2.6
# =====================================================================
@app.get(
    "/api/sismos/moderados", 
    status_code=status.HTTP_200_OK,
    summary="Obtener sismos registrados con magnitud mayor o igual a 2.6"
)
def obtener_sismos_moderados():
    """
    Filtra la lista de diccionarios del extractor, instancia objetos 
    de la clase Sismo para los eventos >= 2.6 y devuelve la respuesta.
    """
    lista_filtrada = []
    
    # Recorremos la lista de diccionarios importada de extractor.py
    for item in lista_diccionarios_final:
        magnitud_evento = item["magnitud(float)"]
        
        # Filtro estricto solicitado: Magnitud mayor o igual a 2.6
        if magnitud_evento >= 2.6:
            
            # Instanciamos el objeto de la clase Sismo importada de seismo.py
            objeto_sismo = Sismo(
                fecha_hora=item["fecha y hora UTC (datetime)"],
                ubicacion=item["Localización(str)"],
                magnitud=magnitud_evento
            )
            
            # Construimos el payload de respuesta. FastAPI convierte automáticamente 
            # el objeto datetime de la clase a un formato string ISO estándar.
            sismo_data = {
                "localizacion": objeto_sismo.ubicacion,
                "fecha_hora_utc": objeto_sismo.fecha_hora,
                "magnitud": objeto_sismo.magnitud,
                "reporte_formateado": objeto_sismo.generar_reporte()  # Ejecuta tu método POO
            }
            lista_filtrada.append(sismo_data)
            
    # Retornamos la estructura de la respuesta
    return {
        "filtro_magnitud_minima": 2.6,
        "total_encontrados": len(lista_filtrada),
        "sismos": lista_filtrada
    }

# Bloque orquestador para ejecutar con 'python api.py' en Arch Linux
if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
