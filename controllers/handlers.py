from flask import render_template, jsonify
import requests

def inicio():
    return render_template('index.html')

def acerca_de_mi():
    return render_template('pages/acerca.html')

def portafolio():
    return jsonify('Estas en la sección de Portafolio')

def contacto():
    return render_template('pages/contacto.html')

def api_handler():
    try:
        API_URL = 'https://reqres.in/api/users?page=1'
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        data = response.json()
        return render_template('api/index.html', miDataUsers=data['data'])
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Error al conectar con la API', 'details': str(e)}), 500
