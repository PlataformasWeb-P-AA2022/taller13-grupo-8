from flask import Flask, render_template
from config import user, password
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/losedificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificios/",
            auth=(user, password))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)


@app.route("/losdepartamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
            auth=(user, password))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("losdepartamentos.html", datos=datos,
    numero=numero)


@app.route("/losdepartamentosdos")
def los_departamentos_dos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
            auth=(user, password))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'nombre_prop':d['nombre_prop'], 
        'costo_dep':d['costo_dep'], 
        'num_cuartos':d['num_cuartos'],
        'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepartamentosdos.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=(user, password))
    nombre = json.loads(r.content)['nombre']
    ciudad = json.loads(r.content)['ciudad']
    cadena = "%s %s" % (nombre, ciudad)
    return cadena
