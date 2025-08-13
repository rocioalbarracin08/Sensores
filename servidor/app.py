from flask import Flask, request
#Necesitamos importa requesta para usarlo recibiendo pedidos

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#No es aceptado por la pagina y por usamos el simulador "postman"
@app.route('/api/sensor', methods = ['POST'])
def sensor():
    nombre = request.json["nombre"] # "request.json": Usado para recibir el diccionario/JSON
    valor = request.json["valor"] # Usamos "request.json["valor"]" para acceder a un valor segun la clave indicada, la clave debe ser la que este en el JSON

    print(f"nombre : {nombre} | valor : {valor}") #Esto se va ver en la terminal
    return "ok" #Esto se mando como response a la página