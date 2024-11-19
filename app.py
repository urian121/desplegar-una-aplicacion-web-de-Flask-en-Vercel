from flask import Flask, redirect, render_template, jsonify, request_started, url_for
import requests #Importando libreria Request para hacer peticiones HTTP
import json #Importando json desde python

app = Flask(__name__)
app.secret_key = '97110c78ae5105da20fe'

@app.route('/')
def inicio():
  return render_template('index.html')


@app.route('/acerca-de-mi')
def acercaDeMi():
    return render_template('pages/acerca.html')


@app.route('/mi-portafolio')
def portafolio():
    return jsonify('Estas en la sección de Portafolio')


@app.route('/contactame')
def contacto():
    return render_template('pages/contacto.html')

@app.route('/api', methods=['GET'])
def api():
    try:
        API_URL = 'https://reqres.in/api/users?page=1'
        response = requests.get(API_URL, timeout=10) # Agregado timeout para evitar bloqueos
        response.raise_for_status() # Lanza un error si el código de estado no es 200

        # Parsear la respuesta JSON
        data = response.json()
        return render_template('api/index.html', miDataUsers=data['data'])
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Error al conectar con la API', 'details': str(e)}), 500

    except Exception as e:
        print(e)

    


#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('inicio'))



if __name__ == '__main__':
  app.run(debug=True, port=5000)