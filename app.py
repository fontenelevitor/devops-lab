from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "API DevOps com Python 🚀"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/hora")
def hora():
    return jsonify({"hora": datetime.now().strftime("%H:%M:%S")})

@app.route("/nome")
def nome():
    return jsonify({"nome": "Vitor"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)