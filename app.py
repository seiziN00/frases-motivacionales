from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

frases = [
    "Sigue avanzando, incluso lento.",
    "Cada error te acerca al éxito.",
    "La disciplina vence al talento.",
    "Hoy es un buen día para empezar.",
    "Construye algo que te haga orgulloso.",
    "Aprender es tu superpoder."
]

@app.route("/api/frase")
def obtener_frase():
    return jsonify({
        "frase": random.choice(frases)
    })

if __name__ == "__main__":
    app.run(debug=True)
