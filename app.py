from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import random, json

app = Flask(__name__)
CORS(app)

# cargar frases
with open("frases.json", "r", encoding="utf-8") as f:
	frases = json.load(f)

def guardar():
	with open("frases.json", "w", encoding="utf-8") as f:
		json.dump(frases, f, ensure_ascii=False, indent=2)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/api/frase", methods=["GET", "POST"])
def frases_api():
	if request.method == "POST":
		data = request.get_json()
		frases.append(data["frase"])
		return {"ok": True}
	return {"frase": random.choice(frases)}

@app.route("/api/stats")
def stats():
	return {"total_frases": len(frases)}


app.run(debug=True)