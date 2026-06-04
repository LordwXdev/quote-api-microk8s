from flask import Flask, jsonify
import socket
import random

app = Flask(__name__)

quotes = [
    "Keep going, you are doing great.",
    "Cloud computing makes apps scalable.",
    "Kubernetes can restart failed containers.",
    "DevOps is about automation and reliability.",
    "Small steps still move the project forward."
]

@app.route("/")
def home():
    return jsonify({
        "quote": random.choice(quotes),
        "pod": socket.gethostname()
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
