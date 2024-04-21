#!/usr/bin/python3
"""
Initializes a Flask web application
must be listening on 0.0.0.0, port 5000
Routes:
    /hbnb_filters
"""

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filter():
    """Defines the hbnb filter"""
    stat = storage.all("State")
    amen = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", stat=stat, amen=amen)


@app.teardown_appcontext
def teardown(excep):
    """Tears down the SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
