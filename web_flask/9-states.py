#!/usr/bin/python3
"""
Initializes a Flask web application
listening on 0.0.0.0, port 5000
Routes:
    /states: display a HTML page: (inside the tag BODY)
    /states/<id>: display a HTML page: (inside the tag BODY)
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Defines an HTML page with a list of all States"""
    st_list = storage.all("State")
    return render_template("9-states.html", st_list=st_list)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Defines an HTML page state with ids"""
    new = storage.all("State")
    for state in new.values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(excep):
    """Tears down the SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
