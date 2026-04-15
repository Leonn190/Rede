from flask import Flask, request, jsonify

app = Flask(__name__)

# começa ligado
estado = {"status": "on"}

@app.route("/")
def home():
    return "API rodando"

@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(estado)

@app.route("/set", methods=["POST"])
def set_status():
    data = request.json

    if "status" in data and data["status"] in ["on", "off"]:
        estado["status"] = data["status"]

    return jsonify(estado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)