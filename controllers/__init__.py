# Importa todas las funciones desde el archivo handlers.py
from .handlers import inicio, acerca_de_mi, portafolio, contacto, api_handler

# Definir qué funciones estarán disponibles al importar controllers
__all__ = ['inicio', 'acerca_de_mi', 'portafolio', 'contacto', 'api_handler']
