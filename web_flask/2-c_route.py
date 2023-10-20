#!/usr/bin/python3
"""
This script builds a Flask application with several routes.
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """
    This route returns a simple "Hello HBNB!" message.
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    This route returns "HBNB" and corresponds to the /hbnb web page.
    """
    return "HBNB"


@app.route('/c/<text>')
def c_route(text):
    """
    This route handles custom URLs and displays "C"
    """
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
