#!/usr/bin/python3
"""
This code initializes a Flask web application
that listens on 0.0.0.0, port 5000.
The route '/' displays 'Hello HBNB!'.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", methods=['GET'])
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
