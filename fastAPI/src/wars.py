import os
from fastapi import FastAPI, HTTPException, status, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title="Acuario universe II", version="1.0.0")

# Lista base (Diccionarios puros)
ESTRELLAS_ACUARIO_LIST = [
    {"id": 1, "name": "Sadalsuud", "type": "Estrella Supergigante", "magnitud": 2.9},
    {"id": 2, "name": "Sadalmelik", "type": "Estrella Gigante Amarilla", "magnitud": 3.6}
]

# ==========================================================================
# 1. ESQUEMAS PYDANTIC
# ==========================================================================
class StarModel(BaseModel):
    id: int = Field(..., description="ID numérico único para la estrella")
    name: str = Field(..., min_length=2, description="Nombre de la estrella")
    type: str = Field(..., description="Clasificación astronómica")
    magnitud: float = Field(0.0, description="Brillo o magnitud aparente")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 3,
                "name": "Deneb Algedi",
                "type": "Estrella Gigante Blanca",
                "magnitud": 2.8
            }
        }
    }

class StarUpdate(BaseModel):
    name: str
    type: str
    magnitud: float  # Cambiado a float para coincidir con la lista base

class StarPatch(BaseModel):
    name: Optional[str] = Field(None, min_length=2, description="Nuevo nombre")
    type: Optional[str] = Field(None, description="Nueva clasificación")
    magnitud: Optional[float] = Field(None, description="Nueva magnitud")

# ==========================================================================
# 2. RUTAS DE LA API
# ==========================================================================

@app.get("/", tags=["Home"])
def home():
    return PlainTextResponse(content='Home')

@app.post("/stars", status_code=status.HTTP_201_CREATED, tags=["Dynamic structure"])
async def create_star(star: StarModel):  # Eliminado el tipado de lista falso
    id_existe = any(elemento["id"] == star.id for elemento in ESTRELLAS_ACUARIO_LIST)
    
    if id_existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La estrella con el ID {star.id} ya se encuentra registrada."
        )
    
    new_star_dict = star.model_dump()
    ESTRELLAS_ACUARIO_LIST.append(new_star_dict)
    
    return {
        "mensaje": "¡Estrella añadida con éxito usando .append()!",
        "elemento_creado": new_star_dict,
        "lista_completa_actualizada": ESTRELLAS_ACUARIO_LIST
    }

@app.get("/stars", tags=["Dynamic structure"])
async def get_stars():
    # Eliminado el .model_dump() erróneo porque ya son diccionarios
    return JSONResponse(content=ESTRELLAS_ACUARIO_LIST, status_code=200)

@app.get("/stars/{id}", tags=["Dynamic structure"])
async def get_star(id: int = Path(..., description="ID de la estrella a buscar", gt=0)): # gt(GreaterThan) validación numérica
    for star in ESTRELLAS_ACUARIO_LIST:
        if star['id'] == id:  # Corregido: 'star_id' cambiado a 'id'
            return JSONResponse(content=star, status_code=200)
    return JSONResponse(content={"error": "Estrella no encontrada"}, status_code=404)

# Corregido: Cambiado GET por PUT y la ruta adaptada a REST
@app.put("/stars/{id}", tags=["Dynamic structure"])
async def update_stars(id: int, star: StarUpdate):
    for item in ESTRELLAS_ACUARIO_LIST:
        if item['id'] == id:  # Corregido a 'id'
            item['name'] = star.name   # Eliminadas las comas finales erróneas
            item['type'] = star.type
            item['magnitud'] = star.magnitud
            return {"mensaje": "Estrella actualizada", "lista": ESTRELLAS_ACUARIO_LIST}
            
    raise HTTPException(status_code=404, detail="Estrella no encontrada para actualizar")


@app.delete("/stars/{id}", tags=["Dynamic structure"])
async def delete_stars(id: int):    
    for star in ESTRELLAS_ACUARIO_LIST:
       if star['id'] == id:
           ESTRELLAS_ACUARIO_LIST.remove(star)
           return JSONResponse(content={"mensaje": "Eliminado", "lista": ESTRELLAS_ACUARIO_LIST})
           
    raise HTTPException(status_code=404, detail="No se encontró la estrella a eliminar")

@app.get('/get_file', tags=["Files"])
def get_file():
    # Nota: Asegúrate de tener un archivo 'file.pdf' en la carpeta o fallará al descargar
    if not os.path.exists('file.pdf'):
        return PlainTextResponse("Simulación: Crea un archivo 'file.pdf' en este directorio para descargarlo.")
    return FileResponse('file.pdf')

@app.patch("/stars/{id}", status_code=status.HTTP_200_OK, tags=["Dynamic structure"])
async def patch_star(id: int, star_data: StarPatch):
    """
    Modifica parcialmente una estrella existente por su ID. 
    Solo se actualizarán los campos que envíes en el JSON body.
    """
    # 1. Buscamos la estrella en la lista
    for star in ESTRELLAS_ACUARIO_LIST:
        if star["id"] == id:
            
            # 2. Convertimos el modelo Pydantic a diccionario, 
            # exclude_unset=True evita que los campos que el usuario no envió pisen con 'None' los datos viejos
            datos_actualizados = star_data.model_dump(exclude_unset=True)
            
            if not datos_actualizados:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, 
                    detail="No has enviado ningún campo válido para modificar."
                )
            
            # 3. Modificación dinámica recorriendo las claves enviadas
            for clave, valor in datos_actualizados.items():
                star[clave] = valor  # actualiza dinámicamente 'name', 'type' o 'magnitud'
                
            return {
                "mensaje": f"Estrella con ID {id} actualizada parcialmente con éxito.",
                "elemento_modificado": star,
                "lista_completa": ESTRELLAS_ACUARIO_LIST
            }
            
    # 4. Si el bucle termina y no encuentra el ID, lanzamos un 404 limpio
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"No se encontró ninguna estrella con el ID {id}."
    )

# Ejecución directa segura
if __name__ == "__main__":
    import uvicorn
    file_name = os.path.basename(__file__).split(".py")[0]
    uvicorn.run(f"{file_name}:app", host="127.0.0.1", port=8000, reload=True)
