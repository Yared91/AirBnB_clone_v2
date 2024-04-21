#!/usr/bin/python3
"""
Intializes a Flask web application.
listens on 0.0.0.0, port 5000.
Routes:
/hbnb_filters: HBnB HTML filters page.
"""
from models import storage
from flask import Flask, render_template
from models import *

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Defines the main HBnB filters HTML page."""
    sta = storage.all("State")
    ameni = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           sta=sta, ameni=ameni)


@app.teardown_appcontext
def teardown(excep):
    """Tears down the SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
