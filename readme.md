# Aplicación de introducción a Flask

Programa hecho en python con el framework Flask, Hello world

## Instalación:
- En su entorno de python ejecutar el comando:
```
pip install -r requirements.txt
```
Las librerías utilizadas Flask en https://flask.palletsprojects.com/en/2/2.x/

## Ejecución del programa:
- Para inicalizar el servidor tenemos que agregar un valor 
    - En mac: ```export FLASK_APP=hello.py```
    - En windows ```set FLASK_APP=hello.py```

## Comando para ejecutar el servidor:
```
flask --app hello run
```

## Comando para que se actualize sin tener que apagar y ejecutar el servidor:
```
flask --app hello --debug run
```

- Se puede dar el caso que el puerto ...../5000 esté ocupado por algun software de nuestro pc. En ese caso hay un comando especial para lanzar el servidor en un puerto diferente:

```
flask --app hello run -p 500
```
```
flask --app hello --debug run -p 5001
```
