from flask import Flask, render_template

app = Flask(__name__) #inicalizar Flask en app

@app.route("/hola") #definimos la ruta donde se va a ejecutar la función
def hola_mundo(): #retorna una string con Hola mundo Flask
    return "Hola mundo Flaskkk"

#Para inicalizar el servidor tenemos que agregar un valor 
    #En mac: export FLASK_APP=hello.py
    #En windows set FLASK_APP=hello.py

#Comando para ejecutar el servidor: flask --app hello run

#Ejercicio: Crear una ruta adiós que retorne una despedida ejemplo: Hasta pronto muchacho

@app.route("/adios")
def despedida():
    return "Hasta pronto, soldadito!"
    #Para que lo reconozca hay que parar el servidor y volver a inicalizarlo --> TRL+C para pararlo 
    #y ejecutar el comando: flask --ap hello run
#EXISTE OTRO COMANDO PARA QUE EL SERVIDOR SE VAYA ACTUALIZANDO SIN TENER QUE PARARLO Y EJECUTARLO OTRA VEZ:
#flask --app hello --debug run

#Se puede dar el caso que el puerto ...../5000 esté ocupado por algun software de nuestro pc
#En ese caso hay un comando especial para lanzar el servidor en un puerto diferente:
#flask --app hello run -p 5001
#flask --app hello --debug run -p 5001


#Ejemplo para enviar parámetros en las rutas
@app.route("/nombre/<n>")
def name(n):
    return f"tu nombre es {n}"
    #(http://127.0.0.1:5001/nombre/Albertito) 


#Ejemplo de realizar una ruta con parámetro que deuvleva el cuadrado de un número:
@app.route("/cuadrado/<num>")
def cuadrado(num):
    num = int(num)
    return f"el cuadrado de {num} es igual a {num * num}"
# o bien 
"""
@app.route("/cuadrado/<int:num>") --> podemos asignar float, str, int...
def cuadrado(num):
    return f"el cuadrado de {num} es igual a {num * num}
"""

#Ejemplo de realizar una ruta que, dinámicamente, pueda realizar operaciones de +, -, *, /. Según
#los parámetros pasados por URL

@app.route("/operacion/<float:n1>/<float:n2>/<ope>")
def calculadora(n1, n2, ope):
    if ope == "suma" or ope == "+":
        return f"La suma es {n1 + n2}"
    if ope == "resta" or ope == "-":
        return f"La resta es {n1 - n2}"
    if ope == "multiplicacion" or ope == "*":
        return f"La multiplicación es {n1 * n2}"
    if ope == "division" or ope == "/": #En este caso el "/" no funcionará por tema de sintaxis en url
        return f"La división es {n1 / n2}"



#Ejemplo de como devolver un html en flask

@app.route("/primerhtml/<nombre>") #http://127.0.0.1:5001/primerhtml/Albertito
def call_html(nombre):
    return render_template("hola.html", name = nombre)



#Calculadora en html:

@app.route("/operacionrender/<float:n1>/<float:n2>/<ope>")
def calculadorarender(n1, n2, ope):

    if ope == "suma" or ope == "+":
        return render_template ("hola.html", resultado = f"La suma de {n1} y {n2} es {n1 + n2}")
    if ope == "resta" or ope == "-":
        return render_template ("hola.html", resultado =  f"La resta de {n1} y {n2} es {n1 - n2}")
    if ope == "multiplicacion" or ope == "*":
        return render_template ("hola.html", resultado =  f"La multiplicación de {n1} y {n2} es {n1 * n2}")
    if ope == "division" or ope == "/": #En este caso el "/" no funcionará por tema de sintaxis en url
        return render_template ("hola.html", resultado = f"La división de {n1} y {n2} es {n1 / n2}")
