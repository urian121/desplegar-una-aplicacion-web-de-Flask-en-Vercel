from controllers import inicio, acerca_de_mi, portafolio, contacto, api_handler


def registrar_rutas(app):
    @app.route('/')
    def ruta_inicio():
        return inicio()

    @app.route('/acerca-de-mi')
    def ruta_acerca_de_mi():
        return acerca_de_mi()

    @app.route('/mi-portafolio')
    def ruta_portafolio():
        return portafolio()

    @app.route('/contactame')
    def ruta_contacto():
        return contacto()

    @app.route('/api', methods=['GET'])
    def ruta_api():
        return api_handler()
