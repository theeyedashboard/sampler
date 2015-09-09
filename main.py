from flask import Flask, Response
import socket
import time
from lib.Sampler import Sampler

app = Flask(__name__)

hostname = socket.gethostname()

@app.route("/")
def index():
    sampler = Sampler()
    return "Sampler running on {}\n".format(sampler.extract())

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=80)
