#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_session(error):
    """closes"""
    storage.close()


@app.route('/states')
@app.route('/states/<id>')
def states_and_cities(id=''):
    """display a HTML page"""
    states = storage.all(State)
    return render_template('9-states.html', id=id, states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
