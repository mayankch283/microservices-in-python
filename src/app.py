from flask import Flask, jsonify, render_template

app = Flask(__name__)

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
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run()