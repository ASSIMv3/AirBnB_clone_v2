#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ return hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Displays the /hbnb web page."""
    return "HBNB"


@app.route('/c/<text>')
def c_route(text):
    """Custom C route with 'C is' followed by text"""
    return "C is {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def py_route(text="is cool"):
    """Custom Python route with 'Python is' followed by text"""
    return "Python is {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """Custom integer route with '<n> is a number'."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def template_number(n):
    """Custom template integer route."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """Custom template to check if a number is odd or even."""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
