from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask!"

@app.route("/about")
def about():
    return "This is a simple CI/CD Demo!"

@app.route("/<name>")
def greet(name):
    return "Hello, {name}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)