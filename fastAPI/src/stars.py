from fastapi import FastAPI, HTTPException, Query, status, Body
from fastapi.responses import JSONResponse
app = FastAPI(title="Acuario universe II", version="1.0.0")

# 🪐 LISTA COMPLEMENTARIA PEQUEÑA (Estructura base)
ESTRELLAS_ACUARIO_LIST = [
    {
        "id": 1,
        "name": "Sadalsuud",
        "type": "Estrella Supergigante",
        "magnitud": 2.9
    },
    {
        "id": 2,
        "name": "Sadalmelik",
        "type": "Estrella Gigante Amarilla",
        "magnitud": 3.6
    }
]

# ==========================================================================
# POST: CREAR ESTRELLA (CON APPEND POR PARÁMETROS)
# ==========================================================================
@app.post("/stars/{star_id}", status_code=status.HTTP_201_CREATED, tags=["Dynamic structure"])
async def create_star(
    star_id: int,
    name: str = Query(..., min_length=2, description="Nombre de la estrella"),
    type: str = Query(..., description="Tipo o clasificación astronómica"),
    magnitud: float = Query(0.0, description="Brillo o magnitud aparente de la estrella")
):
    """
    Crea y añade un nuevo elemento a la lista utilizando .append() 
    basándose en la estructura pasada por parámetros en la URL y Query.
    """
    # 1. CONTROL DE ERRORES (RAISE): Validamos si el ID ya existe en la lista
    id_existe = any(star["id"] == star_id for star in ESTRELLAS_ACUARIO_LIST)
    
    if id_existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La estrella con el ID {star_id} ya se encuentra registrada en la lista."
        )
    
    # 2. SE ARMA LA ESTRUCTURA DINÁMICAMENTE
    new_star = {
        "id": star_id,
        "nombre": name,
        "tipo": type,
        "magnitud": magnitud
    }
    
    # 3. USO DEL APPEND: Inyectamos el diccionario al final de nuestra lista complementaria
    ESTRELLAS_ACUARIO_LIST.append(new_star)
    
    return {
        "mensaje": "¡Estrella añadida con éxito usando .append()!",
        "elemento_creado": new_star,
        "lista_completa_actualizada": ESTRELLAS_ACUARIO_LIST
    }

# ==========================================================================
# GET: OBTENER POR ID (Se ha cambiado la ruta a /stars/{star_id} para no duplicar)
# ==========================================================================
@app.get("/stars", tags=["Dynamic structure"])
async def get_stars_by_id(star_id: int):
    for star in ESTRELLAS_ACUARIO_LIST:
        if star['id'] == star_id:
            return star
    raise HTTPException(status_code=404, detail="Estrella no encontrada")
    #return []

# ==========================================================================
# GET: FILTRAR POR TIPO Y MAGNITUD
# ==========================================================================
# fastAPI ignora por completo la segunda función y colisiona
@app.get("/stars", tags=["Dynamic structure"])
async def stars_by_type(
    tipo: str = Query(min_length=5, max_length=20),
    magnitud: int = Query(..., description="Filtrar por magnitud máxima")
):
    # Buscamos coincidencias aproximadas o exactas
    filtradas = [
        star for star in ESTRELLAS_ACUARIO_LIST 
        if tipo.lower() in star["tipo"].lower() and star["magnitud"] <= magnitud
    ]
    
    if not filtradas:
        return JSONResponse(content={"detail": "Ninguna estrella coincide con el filtro"}, status_code=404)
        
    return filtradas

# ==========================================================================
# PUT: ACTUALIZAR ESTRELLA
# ==========================================================================
@app.put("/stars", status_code=status.HTTP_201_CREATED, tags=["Dynamic structure"])
async def update_star(
    star_id: int = Body(..., embed=True),
    name: str = Body(..., embed=True),
    type: str = Body(..., embed=True),
    magnitud: int = Body(..., embed=True)
    ):

    for star in ESTRELLAS_ACUARIO_LIST:
        if star['id'] == star_id:
            star['name'] = name
            star['type'] = type
            star['magnitud'] = magnitud
            return {'mensaje': F'Estrella {star_id} actualizada', 'lista': ESTRELLAS_ACUARIO_LIST}

    raise HTTPException(status_code=404, detail="No se encontró la estrella para actualizar")

# ==========================================================================
# DELETE: BORRAR ESTRELLA (Requiere recibir un parámetro para saber cuál borrar)
# ==========================================================================
@app.delete("/stars", status_code=status.HTTP_201_CREATED, tags=["Dynamic structure"])
def delete_star(star_id):
    for star in ESTRELLAS_ACUARIO_LIST:
        if star['id'] == star_id:
            ESTRELLAS_ACUARIO_LIST.remove(star)
            return {'mensaje': f'Estrella {star_id} eliminada', 'lista': ESTRELLAS_ACUARIO_LIST}

    raise HTTPException(status_code=404, detail="La estrella no existe en la lista")