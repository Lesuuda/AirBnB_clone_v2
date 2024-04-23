#!/usr/bin/python3
"""This module defines a flask app"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def cities_by_states():
    """Displays a HTML page with a list of states and cities"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_session(exception):
    """Closes the session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
