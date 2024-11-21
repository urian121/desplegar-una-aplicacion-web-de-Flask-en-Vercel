
# Desplegar una aplicación Python/Flask en Vercel 🚀

## Descripción del Proyecto

Esta guía práctica te mostrará cómo desplegar una aplicación web desarrollada con **Python** y **Flask** en **Vercel**. Aprenderás a:

- Configurar el archivo principal de tu aplicación.
- Crear el archivo `vercel.json` necesario para el despliegue.

Ideal tanto para principiantes como para desarrolladores experimentados que buscan una solución rápida y eficiente para hospedar aplicaciones Flask.

---

## Resultado Final

![Resultado Final](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/deploy-web-con-Flask-en-vercel.png)

---

## Explicación del archivo `vercel.json`

Este archivo define cómo Vercel debe desplegar y enrutar tu aplicación Flask.

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### Detalles de la configuración

#### Versión
- `"version": 2`  
  Indica que se utiliza la última versión del sistema de despliegue de Vercel.

#### Bloque `builds`
Define cómo construir tu proyecto antes del despliegue.

- `"src": "app.py"`: Especifica que el archivo principal de tu aplicación es `app.py`.
- `"use": "@vercel/python"`: Utiliza el builder de Python para ejecutar tu aplicación Flask.

#### Bloque `routes`
Configura cómo se gestionan las solicitudes entrantes.

- `"src": "/(.*)"`: Captura cualquier ruta utilizando una expresión regular.
- `"dest": "app.py"`: Redirige todas las solicitudes al archivo `app.py`.

---

## Pasos para el Despliegue

1. **Crear el archivo `requirements.txt`**  
    Este archivo contiene todas las dependencias necesarias para tu aplicación. Para generarlo, ejecuta el siguiente comando:

   ```bash
   pip freeze > requirements.txt
   ```

2. **Crear el archivo `vercel.json`**  
El archivo `vercel.json` debe estar ubicado en la raíz del proyecto. Este archivo es necesario para la configuración del despliegue en Vercel. Asegúrate de que su estructura sea similar a la configuración JSON que se muestra en la parte superior de este README. Aquí es donde se define el comportamiento de tu aplicación en Vercel, como las rutas y el entorno de ejecución.

---

## Consejos Finales

- Asegúrate de que tu archivo `requirements.txt` incluya todas las dependencias necesarias.
- Verifica que tus dependencias sean compatibles con la versión de Python soportada por Vercel.
- Prueba tu aplicación localmente antes de desplegarla.
- Si tu aplicación cuenta con **Variables de Entorno**, las puedes configurar desde el panel de control de Vercel.

🚀 **¡Feliz despliegue!**

---

## Notas Adicionales

- **Archivo `controllers/__init__.py`:**  
  Está configurado para exportar todas las funciones definidas en el archivo `handlers.py`, permitiendo que estén disponibles directamente desde `controllers` al importar.

- **Archivo `routers/__init__.py`:**  
  Está configurado para exportar todas las rutas registradas en el archivo `rutas.py`, facilitando su importación directa desde `routers`.



### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍
