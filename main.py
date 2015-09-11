from flask import Flask, Response, jsonify
import socket
import time
from lib.Sampler import Sampler

app = Flask(__name__)

hostname = socket.gethostname()

@app.route("/")
def index():
    sampler = Sampler()
    return jsonify(sampler.extract())

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=80)
