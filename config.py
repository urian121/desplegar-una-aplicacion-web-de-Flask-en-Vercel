class Config:
    """Configuración base del proyecto con parámetros comunes, como clave secreta, puerto, y base de datos.
    Sirve como clase base para configuraciones específicas de entornos como desarrollo, producción y pruebas.
    """
    SECRET_KEY = '97110c78ae5105da20fe'  # Clave secreta para sesiones
    DEBUG = True  # Activar o desactivar el modo debug
    PORT = 8000  # Puerto de la aplicación
    SESSION_COOKIE_SECURE = False  # Cambiar a True en producción para HTTPS

    # Configuración unificada de la base de datos
    SQLBD = {
        'DATABASE_URI': 'sqlite:///app.db',  # Base de datos SQLite por defecto
        # Descomenta la siguiente línea para usar MySQL
        # 'DATABASE_URI': 'mysql+pymysql://usuario:contraseña@localhost/nombre_base_datos',
        # Descomenta la siguiente línea para usar PostgreSQL
        # 'DATABASE_URI': 'postgresql+psycopg2://usuario:contraseña@localhost/nombre_base_datos',
        'TRACK_MODIFICATIONS': False  # Reducir uso de memoria de SQLAlchemy
    }

# Configuración para producción
class ProductionConfig(Config):
    """Configuración específica para el entorno de producción.
    Desactiva el modo debug y asegura las cookies. Permite configurar una URI de base de datos específica para producción.
    """
    DEBUG = False  # Desactivar modo debug en producción
    SESSION_COOKIE_SECURE = True  # Asegurar cookies en producción
    # Puedes sobrescribir la URI de la base de datos si es diferente en producción
    SQLBD = {
        'DATABASE_URI': 'postgresql+psycopg2://usuario:contraseña@localhost/produccion_db',  # Ejemplo con PostgreSQL
        'TRACK_MODIFICATIONS': False
    }

# Configuración para desarrollo
class DevelopmentConfig(Config):
    """Configuración específica para el entorno de desarrollo.
    Habilita el modo debug para facilitar la depuración durante el desarrollo.
    """
    DEBUG = True  # Activar modo debug en desarrollo


# Configuración para pruebas
class TestingConfig(Config):
    """Configuración específica para pruebas."""
    TESTING = True  # Activar modo pruebas
    DEBUG = True  # Activar modo debug en pruebas
    # Puedes sobrescribir la URI de la base de datos para pruebas
    SQLBD = {
        'DATABASE_URI': 'sqlite:///test.db',  # Base de datos para pruebas (SQLite)
        'TRACK_MODIFICATIONS': False
    }
