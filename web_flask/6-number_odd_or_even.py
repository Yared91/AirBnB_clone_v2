#!/usr/bin/python3
"""
Initializes a Flask web application
listening on 0.0.0.0, port 5000
Route:
    /Hello HBNB
    /hbnb
    /c/<text>
    /python/<text>
    /number/<n>
    /number_template/<n>
    /number_odd_or_even/<n>
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Defines 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Defines 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Defines 'C' followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoncool(text='is cool'):
    """Defines "Python ", followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def numbers(n):
    """Defines n is a number only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """Display  a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """Defines a HTML page only if n is an integer"""
    num = "even" if (n % 2 == 0) else "odd"
    return render_template("6-number_odd_or_even.html", n=n, num=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
