#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(request):
    """Closes"""
    storage.close()


@app.route('/cities_by_states')
def cities():
    """display a HTML page"""
    states = storage.all(State)
    cities = storage.all(City)
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
