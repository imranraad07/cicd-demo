from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask!"

@app.route("/about")
def about():
    return "This is a simple CI/CD Demo!"


if __name__ == "__main__":
    app.run()