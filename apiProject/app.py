# let's import the flask
from flask import Flask, render_template, Response
import os # importing operating system module
import pymongo
MONGODB_URI = 'mongodb://barcoAmarillo:Password@localhost.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())
db = client['usuarios']

students = [
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

for student in students:
    # Para MongoDB:
    #db.students.insert_one(student) # riesgo de inserción doble: Cuando usas debug=True, Flask activa un mecanismo llamado reloader (recargador automático). Este sistema arranca el script principal dos veces: la primera vez para lanzar el proceso principal y la segunda para el proceso de depuración que vigila si haces cambios en el código. Como tu lógica de inserción de datos está suelta en el cuerpo del script, se ejecuta en ambos arranques.
    db.students.update_one({'name': student['name']}, {'$set': student}, upsert=True) # nos aseguramos de que sólo se inserte una vez

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=port)