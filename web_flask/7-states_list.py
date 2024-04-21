#!/usr/bin/python3
"""
Initializes a Flask web application
listening on 0.0.0.0, port 5000
Route:
    /states_list
"""

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route("/states_list",  strict_slashes=False)
def states_cities():
    """Defines an HTML page with list of all State in DBStorage"""
    st_lt = storage.all("State").values()
    return render_template("7-states_list.html", st_lt=st_lt)


@app.teardown_appcontext
def teardown(excep):
    """Tears down the SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
