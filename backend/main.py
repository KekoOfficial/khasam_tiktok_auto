from flask import Flask, request, jsonify, send_from_directory
from cutter import cortar_video
from uploader import subir_videos
import json
import os

app = Flask(__name__, static_folder="../frontend", template_folder="../frontend")

# Cargar configuración
with open("config.json") as f:
    config = json.load(f)

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/start', methods=['POST'])
def start():
    data = request.get_json()
    titulo = data['titulo']

    # 1️⃣ Cortar video
    cortar_video("../input/video.mp4", config["duracion_video"])

    # 2️⃣ Subir automáticamente
    subir_videos(titulo, config)

    return jsonify({"message": "Sistema iniciado: corte + subida automática"})

@app.route('/style.css')
def style():
    return send_from_directory('../frontend', 'style.css')

@app.route('/script.js')
def script():
    return send_from_directory('../frontend', 'script.js')

if __name__ == "__main__":
    app.run(debug=True)