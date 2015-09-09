from flask import Flask, Response
import socket
import time

app = Flask(__name__)

hostname = socket.gethostname()

@app.route("/")
def index():
    return "Sampler running on {}\n".format(hostname)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=80)
