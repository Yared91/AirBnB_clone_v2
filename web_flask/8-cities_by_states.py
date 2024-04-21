#!/usr/bin/python3
"""
Initializes a Flask web application
listening on 0.0.0.0, port 5000
Routes:
    /cities_by_states
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states",  strict_slashes=False)
def cities_states():
    """Defines an HTML page with list of all State in DBStorage"""
    sta_list = storage.all("State").values()
    return render_template("8-cities_by_states.html", sta_list=sta_list)


@app.teardown_appcontext
def teardown(excep):
    """Tears down the SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
