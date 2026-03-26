from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/multiply")
def multiply():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    return jsonify({"result": a * b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)