#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Return a simple hello message."""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Display the /hbnb web page."""
    return "HBNB"


@app.route('/c/<text>')
def c_route(text):
    """Custom C route displaying 'C is' followed by the input text"""
    return "C is {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def py_route(text="is cool"):
    """Custom Python route displaying 'Python is'"""
    return "Python is {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """Display the input number with ' is a number'."""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
