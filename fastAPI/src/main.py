from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import HTMLResponse # permite inyectar contenido HTML que queremos enviar

"""
OpenAPI cuya documentación técnica (acceso: 127.0.0.1:8000/docs) muestra schema de Swagger.
El estándar de OpenAPI reconoce datos primitivos (object, array, string, integer).
Al registrar HTMLResponse avisa al navegador que el medio es text/html pero en la documentación
técnica (127.0.0.1:8000/docs) devuelve un string.
"""

app = FastAPI()

app.title = "Aquarius universe"

app.version = '1.0.0'

# Estructura para la documentación de HTML en Swagger que se devuelve gracias a 'responses' en la función 'see'
html_docs = {
    200: {
        "description": "Devuelve la página web de administración del acuario",
        "content": {
            "text/html": {
                "example": "<!-- Muestra de código de salida -->\n<html><body><h1>🐋 Aquarius Universe</h1></body></html>"
            }
        }
    }
}

# 🪐 DICCIONARIO DE DATOS: Características de Saturno en Acuario
SATURNO_ACUARIO_DATA = {
    1: {
        "concepto": "Significado Astrológico",
        "descripcion": "Saturno está en su domicilio tradicional en Acuario. Representa la estructura mental, la disciplina social, el pensamiento humanitario objetivo y la capacidad de materializar ideas revolucionarias o tecnológicas.",
        "palabras_clave": ["Estructura", "Innovación", "Objetividad", "Comunidad"]
    },
    2: {
        "concepto": "Lección de Vida",
        "descripcion": "Aprender a colaborar en grupo sin perder la individualidad. Romper estructuras obsoletas mediante la razón, la responsabilidad social y el desarrollo tecnológico ético.",
        "desafio": "Evitar el desapego emocional extremo o la tozudez ideológica."
    },
    3: {
        "concepto": "Rasgos de Personalidad Natal",
        "descripcion": "Individuos con una mente científica, visionaria y altamente organizada. Suelen ser excelentes planificadores a largo plazo en proyectos comunitarios o de vanguardia.",
        "madurez": "Se consolida notablemente a partir del primer retorno de Saturno (aprox. a los 29 años)."
    },
    4: {
        "concepto": "Astronomía y Ciclos",
        "descripcion": "Saturno tarda aproximadamente 29.5 años en dar la vuelta al Sol. Su última estancia en la constelación/signo de Acuario ocurrió recientemente entre los años 2020 y 2023.",
        "elemento": "Aire (Fijo)"
    }
}

@app.get("/", tags=['Home']) # con tags le asigno orgen; sin [] fragmenta la palabra por letras
async def read_root():
    return {"Hello": "World"}

@app.get("/home/", response_class=HTMLResponse, responses=html_docs, tags=['Home'])
async def see():

    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Aquarius universe</title>
        <style>
            body { 
                font-family: sans-serif; 
                background-color: #121212; 
                color: #e0e0e0; 
                text-align: center; 
                padding: 3rem;
            }
            h1 { color: #00d2ff; }
            .fluid-card { 
                border: 1px solid #333; 
                padding: 1.5rem; 
                border-radius: 8px; 
                max-width: 400px; 
                margin: 2rem auto; 
            }
        </style>
    </head>
    <body>
        <h1>🐋 Bienvenido a Acuario Universe</h1>
        <p>Este HTML se está generando de forma dinámica inyectado desde Python.</p>
        
        <div class="fluid-card">
            <h3>Estado del Tanque Principal</h3>
            <p>Temperatura: 24°C | pH: 8.2</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/items/{item_id}", tags=['Aquarius Saturn']) # Paso de estructura por Ruta
async def read_item(item_id: int, q: str | None = Query(None, description="Filtro de búsqueda opcional")):
    # 1. Buscamos el elemento en nuestro diccionario de características
    caracteristica = SATURNO_ACUARIO_DATA.get(item_id)

    # 2. Si el ID no existe en el diccionario, lanzamos un error 404 limpio
    if not caracteristica:
        raise HTTPException( # lanza una excepción controlada para no detener el código al introducir un valor no válido
            status_code=404, # 'Not found'
            detail=f"ID {item_id} no encontrado. Prueba con un identificador del 1 al {len(SATURNO_ACUARIO_DATA)}."
        )
    # 3. Preparación de la respuesta base
    respuesta = {
        "item_id": item_id,
        "datos": caracteristica
    }
    
    # 4. Lógica para el parámetro opcional 'q' (si el usuario escribe algo en Swagger)
    if q:
        respuesta["filtro_aplicado"] = q
        # Comprobación básica: ¿el filtro coincide con alguna palabra del concepto?
        respuesta["coincide_filtro"] = q.lower() in str(caracteristica).lower()

    return {"item_id": item_id, "q": q}


@app.post("/items", tags=['Aquarius Saturn']) # Paso de estructura por Ruta
def create_item(item_id: int):
    
    return
"""

PARA ACTIVAR EL ENTORNO VIRTUAL REQUERIDO PARA FASTAPI:
1. cd fastAPI
2. python -m venv .venv
3. source .venv/bin/activate
4. pip install "fastapi[standard]" o pip install fastapi uvicorn
* Si no aparece (.nenv)' al principio de línea en terminal del directorio: 
    echo $VIRTUAL_ENV ----> Si devuelve: /home/alumnom/arquitectura-cliente-servidor/fastAPI/.venv      ESTÁ ACTIVADO, la terminal oculta gráficamente por configuración visual personalizada de Sistema Operativo
                      ----> Si se queda en blanco: el entorno virtual NO está activado; ejecutar: source ./.venv/bin/activate

Para ejecutar el programa: fastapi dev main.py o uvicorn main:app

Si el puerto por defecto (8000) que utiliza FastAPI está utilizado cambiar a uno libre:
    fastapi dev main.py --port 8080 (comando FastAPI)
                o
    uvicorn main:app --reload --port 8080 (comando Uvicorn)

Alternativa, matar el proceso que bloquea el puerto 8000:
    fuser -k 8000/tcp ()

Acceso al servidor:
    url: 127.0.0.1:8000

Para acceder a la documentación (autodocumentada):
    url: 127.0.0.1:8000/docs

*****************************************************************************************
* Uvicorn es el motor o servidor web de alto rendimiento que se encarga de ejecutar     *
* las aplicaciones construidas con FastAPI. Le aporta velocidad y asincronía gracias al *
* estándar ASGI (Asynchronous Server Gateway Interface) (asincronía) y estar programado *
* en C utilizando 'uvloop' (rapidez).                                                   *
*****************************************************************************************

"""