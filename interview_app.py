
import os 
from flask import Flask, jsonify, request 

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "<h1>Welcome to my App!!</h1>", 200

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)
