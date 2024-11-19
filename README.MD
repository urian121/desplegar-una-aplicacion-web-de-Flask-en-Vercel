# Cómo desplegar una aplicación Python/Flask en Vercel 🚀

####  Descripción del Proyecto

Este proyecto es una guía práctica que muestra cómo desplegar una aplicación web construida con **Python** y **Flask** en los servidores de **Vercel**. Aquí aprenderás a configurar el archivo principal de tu aplicación, crear el archivo `vercel.json` para el despliegue, y utilizar la CLI de Vercel para llevar tu proyecto a producción de manera rápida y eficiente. 

La guía está diseñada para ser sencilla y accesible, ideal tanto para principiantes como para desarrolladores que buscan una solución rápida para hospedar sus aplicaciones Flask.

¡Sigue los pasos y haz que tu aplicación esté disponible al mundo en cuestión de minutos! 🚀


# Explicación del archivo `vercel.json`

Este archivo configura el despliegue de una aplicación Flask en Vercel.

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

### Explicando el archivo `vercel.json`

- ```"version": 2```
    Indica que estamos utilizando la versión 2 del sistema de despliegue de Vercel. Esta versión es la más reciente y adecuada para configurar aplicaciones modernas.

### Bloque builds

Define cómo se construye el proyecto antes del despliegue.
- ```"builds": [ ```
Inicia la definición de los pasos de construcción del proyecto.
- ```"src": "app.py"```
Especifica que el archivo principal de la aplicación es app.py. Este archivo debe contener el código principal de tu aplicación Flask.
- ```"use": "@vercel/python"```
Indica que se utiliza el builder de Python de Vercel (@vercel/python) para ejecutar la aplicación.

### Bloque routes
Configura cómo se redirigen las solicitudes entrantes.

- ```"routes": [ ```
Inicia la definición de las reglas de enrutamiento.
- ```"src": "/(.*)"```
Especifica una expresión regular para capturar cualquier ruta de solicitud.El ```(.*)``` captura todo después del /.
- "dest": "app.py"
Indica que todas las solicitudes capturadas por "src" deben ser manejadas por app.py.


### Crea un archivo `requirements.txt`
Incluye todas las dependencias necesarias de tu aplicación. Puedes generarlo con:

```bash
pip freeze > requirements.txt
```


## Configuraciones Adicionales

### Variables de Entorno

Puedes configurarlas en:
- Vercel Dashboard
- CLI de Vercel:

```bash
  vercel env add VARIABLE_NAME valor
```

## Consejos Finales

- Asegúrate de que `requirements.txt` esté completo
- Verifica compatibilidad de dependencias
- Realiza pruebas locales antes del despliegue

🚀 **¡Feliz despliegue!**
