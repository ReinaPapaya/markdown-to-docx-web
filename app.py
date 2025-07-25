# app.py
from flask import Flask, request, render_template, send_file, flash, redirect, url_for
import os
import tempfile
from converter import MarkdownConverter # Importa la lógica del conversor

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui' # Cambia esto por una clave segura en producción

# Instancia del conversor
converter = MarkdownConverter()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Verificar si se envió un archivo markdown
        if 'markdown_file' not in request.files:
            flash('No se seleccionó ningún archivo Markdown.')
            return redirect(request.url)
        markdown_file = request.files['markdown_file']

        # Verificar si el nombre del archivo está vacío
        if markdown_file.filename == '':
            flash('No se seleccionó ningún archivo Markdown.')
            return redirect(request.url)

        if markdown_file:
            try:
                # Crear un directorio temporal para trabajar
                with tempfile.TemporaryDirectory() as tmpdirname:
                    # Guardar el archivo markdown subido
                    md_path = os.path.join(tmpdirname, markdown_file.filename)
                    markdown_file.save(md_path)

                    # Opcional: manejar la plantilla (si decides implementarla)
                    # template_file = request.files.get('template_file')
                    # template_path = None
                    # if template_file and template_file.filename != '':
                    #     template_path = os.path.join(tmpdirname, template_file.filename)
                    #     template_file.save(template_path)

                    # Leer el contenido del markdown
                    with open(md_path, 'r', encoding='utf-8') as f:
                        md_content = f.read()

                    # Parsear elementos
                    elements = converter.parse_markdown_elements(md_content)

                    # Definir la ruta del archivo de salida DOCX
                    output_filename = os.path.splitext(markdown_file.filename)[0] + ".docx"
                    output_path = os.path.join(tmpdirname, output_filename)

                    # Convertir a DOCX (sin plantilla en esta versión simplificada)
                    converter.convert_to_docx(elements, output_path)

                    # Enviar el archivo generado al usuario
                    return send_file(output_path, as_attachment=True, download_name=output_filename)

            except Exception as e:
                flash(f'Error al convertir el archivo: {str(e)}')
                # Para depuración, puedes imprimir el traceback completo en logs del servidor
                # import traceback
                # app.logger.error(traceback.format_exc())
                return redirect(request.url)

    # Si es GET o si hay un error, mostrar el formulario
    return render_template('index.html')

if __name__ == '__main__':
    # En Render, la variable PORT se define automáticamente
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) # host='0.0.0.0' es importante para Render
