#!/usr/bin/python3
"""
Task 4 script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello(strict_slashes=False):
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb(strict_slashes=False):
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text, strict_slashes=False):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def print_int(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
