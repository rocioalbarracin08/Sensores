import sqlite3
from flask import Flask, request, g
#Necesitamos importa requesta para usarlo recibiendo pedidos

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def dict_factory(cursor, row):
 """Arma un diccionario con los valores de la fila."""
 fields = [column[0] for column in cursor.description]
 return {key: value for key, value in zip(fields, row)}


def abrirConexion():
  if 'db' not in g:
     g.db = sqlite3.connect("valores.sqlite")
     g.db.row_factory = dict_factory
  return g.db


def cerrarConexion(e=None):
   db = g.pop('db', None)
   if db is not None:
       db.close()

#No es aceptado por la pagina y por usamos el simulador "postman"
@app.route('/api/sensor', methods = ['POST'])
def sensor():
    db = abrirConexion()
    nombre = request.json["nombre"] # "request.json": Usado para recibir el diccionario/JSON
    valor = request.json["valor"] # Usamos "request.json["valor"]" para acceder a un valor segun la clave indicada, la clave debe ser la que este en el JSON
    
    #Insertarlo en la base de datos
    db.execute("""INSERT INTO valores(nombre, valor) VALUES (?,?)""", (nombre,valor))
    db.commit() #Cierra la transaccion

    print(f"nombre : {nombre} | valor : {valor}") #Esto se va ver en la terminal
    db = cerrarConexion()

    return "ok" #Esto se mando como response a la página