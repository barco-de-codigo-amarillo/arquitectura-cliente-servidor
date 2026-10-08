# arquitectura-cliente-servidor
About three layers

This code is part of a beginner Python training. The corresponding practice is run at the end of each block.

# API de Automatización de Programas Python

Una API REST robusta construida con **FastAPI** y conectada a una base de datos **MariaDB**. El proyecto comenzó como un conjunto de scripts en Python que describían y probaban diferentes lógicas con el código, evolucionando finalmente en una API de producción lista para ser desplegada con **Uvicorn**.

## Tecnologías Utilizadas

* **Python:** Lenguaje principal para la lógica del negocio y scripts iniciales.
* **FastAPI:** Framework web moderno y de alto rendimiento para la creación de la API.
* **MariaDB:** Base de datos relacional para el almacenamiento de datos.
* **Uvicorn:** Servidor ASGI rápido para ejecutar la aplicación FastAPI.

## Características

* **Pruebas de concepto integradas:** Programas en Python que documentan y ejecutan las distintas posibilidades de la lógica del código.
* **API RESTful:** Endpoints optimizados para interactuar con los datos de forma segura.
* **Documentación Interactiva:** Generación automática de swagger UI (`/docs`) gracias a FastAPI.
* **Rendimiento Asíncrono:** Aprovechamiento total de las capacidades `async` de Python y Uvicorn.

## Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### 1. Prerrequisitos
Asegúrate de tener instalado **Python 3.x** y una instancia de **MariaDB** ejecutándose.

### 2. Clonar el repositorio
```bash
git clone https://github.com
cd tu-repositorio
```

### 3. Crear y activar un entorno virtual
```bash
# En Linux/macOS
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### 4. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 5. Configurar las variables de entorno
Crea un archivo `.env` en la raíz del proyecto y añade tus credenciales de MariaDB:
```env
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=nombre_base_datos
DB_PORT=3306
```

## Uso

### Ejecutar los scripts de prueba (Lógica de código)
Si deseas probar las diferentes posibilidades del código base antes de lanzar la API, ejecuta:
```bash
python nombre_de_programa.py
```

### Levantar el servidor de la API
Para iniciar la API con recarga automática en desarrollo usando **Uvicorn**:
```bash
uvicorn main:app --reload
```
_Nota: Reemplaza `main:app` si el archivo principal de tu API tiene otro nombre._

Una vez encendido el servidor, puedes acceder a la documentación interactiva en:
* **Swagger UI:** http://127.0.0
* **ReDoc:** http://127.0.0

## Licencia

Este proyecto está bajo la Licencia GPLv3. Consulta el archivo `LICENSE` para más detalles.
