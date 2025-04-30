from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hi! this is a Flask App created by me!"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/test-error")
def test_error():
    x = 1/0
    return "This won't work!"

@app.errorhandler(500)
def handle_error(error):
    return "Oops! Something went wrong."


if __name__ == '__main__':
    app.run()