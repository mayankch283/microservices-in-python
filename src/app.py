from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

def fetchDetails():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip

@app.route("/")
def greet():
    return "<p>Hello, world!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname, ip = fetchDetails()
    return render_template("index.html", HOSTNAME=hostname, IP=ip)
    
if __name__ == "__main__":
    app.run()