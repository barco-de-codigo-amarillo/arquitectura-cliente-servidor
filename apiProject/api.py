from datetime import datetime
import os
from flask import Flask,  Response, request
import pymongo
import json
from bson import ObjectId
from bson.json_util import dumps # cada vez que se vea un dumps en código se hace este y no el "natural" del módulo json

app = Flask(__name__)

MONGODB_URI = "mongodb://administrador:admin123@localhost:27017/desarrollo?authSource=admin"
#Nota: nunca incluyas credenciales reales en el código.
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos
# Este entry-point es para que el usuario (via CLI o navegador o desde un proceso almacenado) acceda a todos los documentos "json" de STUDENTS
# GET de todos
@app.route('/api/v1.0/students', methods = ['GET'])
def students():
    students_cursor = db.students.find({}) # .find() devuelve un objeto especial llamado 'Cursor'
    # json_util.dumps transforma el cursor completo automáticamente 
    return Response(dumps(students_cursor), mimetype='application/json')


# Este entry-point es para que el usuario (via CLI o navegador o desde un proceso almacenado) acceda a un STUDENT con id específico.
# GET de uno concreto
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student(id):
    # .find_one() devuelve el documento directamente como diccionario o None (NO un cursor)
    student = db.students.find_one({'_id':ObjectId(id)}) # Busca un elemento único por 'id' en 'Students'

    if student is None:
        return Response(dumps({"error": "Estudiante no encontrado"}), status = 404, mimetype='application/json')
    
    return Response(dumps(student), mimetype='application/json')

"""
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student_1():
    name = "Juan"#request.form['name']
    country = "Argentina" #request.form['country']
    city = "Rosario" #request.form['city']
    skills = ["Java", "HTML", "SQL"] #request.form['skills'].split(', ')
    bio = "Experiencia en Front End de 2 años, y 3 en Back End"#request.form['bio']
    birthyear = 2001#request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }
    db.students.insert_one(student)
    return
#create_student()_1 # es posible aunque aberrante y ridículo, puesto que el servidor no tiene la función de autoinvocarse. Aquí no hay participación de acción de cliente
"""

#POST: crea uno nuevo
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }
    db.students.insert_one(student)
    # Devuelve (Response) un texto plano /JSON que devuelve una respuesta con una cabecera HTTP crucial para el navegador
    return Response(dumps({"resultado":"se ha creado un nuevo estudiante"}), mimetype='application/json')

# PUT: modifica uno existente
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # este decorador crea la ruta para actualizar
def update_student (id):
    # Crea un diccionario de consulta diseñado específicamente para buscar un documento único dentro de MongoDB utilizando su 'id'
    query = {"_id":ObjectId(id)}
    # extrae el valor que un usuario escribió en un formulario web HTML y que fue enviado hacia el servidor Flask mediante método POST o PUT
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }

    # operador nativo '$set' modifica, establece o actualiza el objeto 'student' del diccionario 'students'
    db.students.update_one(query, {"$set": student}) # 'query' pasa el 'id'
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return Response(dumps({f'"resultado":"se ha actualizado el documento con id" {id}'}), mimetype='application/json')


# DELETE uno concreto por id
@app.route('/api/v1.0/students/<id>', methods = ['DELETE'])
def delete_student(id):
    db.students.delete_one({"_id":ObjectId(id)})
    return Response(dumps({f'/"resultado/":/"se ha borrado el documento con id/" {id}'}), mimetype='application/json')


if __name__ == '__main__':
    # usado en despliegue
    # para que funcione en producción y desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=port)


"""
from flask import Flask, jsonify, abort
from bson.objectid import ObjectId  # Crucial para buscar por ID en MongoDB
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["academia_db"]
coleccion = db["students"]

# TU RUTA:
@app.route('/api/v1.0/students/<id>', methods=['GET'])
def get_student(id):
    try:
        # MongoDB usa un tipo de dato especial llamado ObjectId para sus IDs de texto
        student = coleccion.find_one({"_id": ObjectId(id)})
        
        if student is None:
            abort(404) # Si no existe el alumno, manda un error 404
            
        # Modificamos el campo _id para convertirlo a texto antes de enviarlo por JSON
        student["_id"] = str(student["_id"])
        
        # Devuelve los datos del estudiante en formato JSON limpio
        return jsonify(student)
        
    except Exception:
        # Si el ID enviado en la URL no tiene el formato correcto de MongoDB, da error
        abort(400) 

"""