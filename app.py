from flask import Flask, redirect, url_for
# Importando todas las rutas desde Routers
from routers import registrar_rutas
# Importando la configuración del proyecto
from config import Config, DevelopmentConfig

app = Flask(__name__)

"""
Cargar la configuración desde el archivo config.py
El método from_object() de Flask se utiliza para cargar la configuración de una aplicación Flask a partir de una clase u objeto Python.
"""
app.config.from_object(DevelopmentConfig)
# print(app.config['SQLBD']['DATABASE_URI']) # Esto imprime la URI de la base de datos configurada
print(f"Secret Key: {app.config['SECRET_KEY']}") # Esto imprime la clave secreta configurada (en este caso, app.config['SECRET_KEY'])
print(f"Debug: {app.config['DEBUG']}")

# Registrar las rutas desde el archivo externo
registrar_rutas(app)


# Manejo de error 404
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('ruta_inicio'))


if __name__ == '__main__':
    # Accede directamente a las configuraciones de Config en lugar de app.config
    app.run(debug=Config.DEBUG, port=Config.PORT)
