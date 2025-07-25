# Conversor Markdown a DOCX (Versión Web)

Esta es una aplicación web simple que convierte archivos Markdown (`.md`) a documentos de Microsoft Word (`.docx`).

## Cómo usar

1.  Accede a la aplicación web.
2.  Haz clic en "Selecciona tu archivo Markdown".
3.  Elige el archivo `.md` que deseas convertir.
4.  Haz clic en el botón "Convertir a DOCX".
5.  El navegador iniciará la descarga del archivo `.docx` convertido.

## Despliegue en Render

1.  Crea un repositorio en GitHub con estos archivos.
2.  Regístrate/Inicia sesión en [https://render.com](https://render.com).
3.  Crea un nuevo "Web Service".
4.  Conecta tu repositorio de GitHub.
5.  Configura el servicio:
    *   **Name:** Elige un nombre para tu servicio.
    *   **Runtime:** Python 3.
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `gunicorn app:app` (necesitarás agregar `gunicorn` a `requirements.txt`: `echo "gunicorn" >> requirements.txt`)
6.  Haz clic en "Create Web Service".

La aplicación se desplegará automáticamente.
