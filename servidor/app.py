from flask import Flask, render_template ,url_for
import sqlite3

app = Flask(__name__)

db = None

@app.route("/") #Devuelve lo que ve en el navegador
def principal():
    url_saludo = url_for("saludoxnombre", nombre='Rocío')
    return f"""
        <a href="{url_saludo}">Saludo por nombre</a>
    """

@app.route("/hola/<string:nombre>") 
def saludarxnombre(nombre):
    return f"<h2> Hola {nombre}! </h2>"