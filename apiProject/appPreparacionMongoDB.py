from flask import Flask,  Response
import json
import pymongo
import os
# conexión a mi MongoDB
MONGODB_URI = 'mongodb://barcoAmarillo:Password@localhost.mongodb.net/test?retryWrites=true&w=majority'

#Nota: nunca incluyas credenciales reales en el código.
# Aquí creo un cliente a MongoDB
client = pymongo.MongoClient(MONGODB_URI)
# Creación de BBDD con acceso cliente
db = client['usuarios'] # acceder a la base de datos
# Este entry-point es para que el usuario (via CLI o navegador o desde un proceso almacenado) acceda a todos los documentos "json" de Usuarios

app = Flask(__name__)

usuarios = [
    {
        "name": "Alejandro Martínez",
        "country": "España",
        "city": "Zaragoza",
        "age": 22
    },
    {
        "name": "Elena Rostova",
        "country": "Argentina",
        "city": "Buenos Aires",
        "age": 25
    },
    {
        "name": "Liam Gallagher",
        "country": "Reino Unido",
        "city": "Manchester",
        "age": 21
    },
    {
        "name": "Yuki Tanaka",
        "country": "Japón",
        "city": "Tokio",
        "age": 24
    },
    {
        "name": "Mateo Silva",
        "country": "Chile",
        "city": "Santiago",
        "age": 23
    }
]


for usuario in usuarios:
    @app.route('/api/v1.0/usuarios', methods = ['GET'])
    def students ():
        #db.students.insert_one(student) # riesgo de inserción doble: Cuando usas debug=True, Flask activa un mecanismo llamado reloader (recargador automático).
        # Este sistema arranca el script principal dos veces: la primera vez para lanzar el proceso principal y la segunda para el proceso de depuración que vigila si haces cambios en el código. Como tu lógica de inserción de datos está suelta en el cuerpo del script, se ejecuta en ambos arranques.
        db.students.update_one({'name': usuario['name']}, {'$set': usuario}, upsert=True) # nos aseguramos de que sólo se inserte una vez

estudiante = db.usuarios.find_one()


if __name__ == '__main__':
    # usado en despliegue
    # para que funcione en producción y desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=port)