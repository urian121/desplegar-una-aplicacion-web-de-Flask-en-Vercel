from flask import Flask, redirect, url_for
# Importando todas las rutas desde Routers
from routers import registrar_rutas


app = Flask(__name__)
app.secret_key = '97110c78ae5105da20fe'

# Registrar las rutas desde el archivo externo
registrar_rutas(app)

# Manejo de error 404
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('ruta_inicio'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
