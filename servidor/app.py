import sqlite3
from flask import Flask, request, g
from math import ceil
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
     g.db = sqlite3.connect("valores.sqlite") #Depende del archivo sqlite
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

    return {"Resultado": "ok"} #Mensaje jsonificado automaticamente, sin usar "jsonify"

#Actividad 16
resultados_por_pag = 2

@app.route('/api/lista')
def listaValores():
   db = abrirConexion()

   args = request.args
   pagina = int(args.get('page', '1')) #Para reconocer el número de página en el que esta la persona (el "()" dice...)
   descartar = (pagina-1) * resultados_por_pag #Al empezar en la página 1 es necesario restarle una pag para no descartar su misma cantidad y quedarnos sin página(si empezaramos a contar desde 0 no haria falta) 
   db = abrirConexion()

   #Para contar la cantidad de regique hay
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM artists;")

   cant = cursor.fetchone()['cant'] #Devolvemos el resultado de la columna cant(creada cuando se realiza el COUNT)
   paginas = ceil(cant / resultados_por_pag) #Responde a cuantas visualizaciones de registro van haber por página

   if pagina < 1 or pagina > paginas:
      return f"Página inexistente: {pagina}", 400
   

   db = cerrarConexion()