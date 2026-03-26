from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Arithmetic Microservices</h1><p>Use /add or /multiply with a and b</p>"

@app.route("/add")
def add():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    response = requests.get(f"http://addition:5000/add?a={a}&b={b}")
    return jsonify(response.json())

@app.route("/multiply")
def multiply():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    response = requests.get(f"http://multiplication:5000/multiply?a={a}&b={b}")
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)