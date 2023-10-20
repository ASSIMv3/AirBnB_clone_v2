#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """Prints 'Hello HBNB'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints 'HBNB'."""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """Prints 'C' followed by <text>. Replaces underscores with spaces."""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """Prints 'Python' followed by <text>. Replaces underscores with spaces."""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Displays <n> if it's an integer."""
    return "%i is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page if <n> is an integer."""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
