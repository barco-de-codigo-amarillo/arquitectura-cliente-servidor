from flask import Flask, render_template, abort
import os

app = Flask(__name__)

POSTS_DB = {
    1: {
        "titulo": "Mi primer post en Flask",
        "fecha": "22 de Septiembre, 2026",
        "autor": "Desarrollador Arch",
        "contenido": "¡Hola desde el entorno virtual! Este es el cuerpo de mi primer artículo. Flask y Jinja hacen que renderizar páginas web dinámicas con Python sea extremadamente limpio y sencillo."
    },
    2: {
        "titulo": "Configurando entornos en Arch Linux",
        "fecha": "23 de Septiembre, 2026",
        "autor": "Admin Linux",
        "contenido": "En este post aprenderás por qué los entornos virtuales (<code>.venv</code>) son cruciales en sistemas como Arch Linux para mantener tus dependencias de desarrollo aisladas del sistema operativo global."
    }
}

@app.route('/')
def home():
    return render_template('home.html', posts=POSTS_DB)

@app.route('/about')
def about():
    return render_template('about.html', posts=POSTS_DB)

@app.route('/post/<int:post_id>')
def ver_post(post_id):
    # Corrección del TypeError aquí:
    post = POSTS_DB.get(post_id)
    if post is None:
        abort(404)
    return render_template('post.html', post=post, posts=POSTS_DB)

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('404.html', posts=POSTS_DB), 404

if __name__ == '__main__':
    # Usamos el puerto 5001 por si el 5000 sigue bloqueado en tu sistema
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=port)
