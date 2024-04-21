#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route /
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route /hbnb
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route /c/<text>
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    Route /python/<text>
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>/', strict_slashes=False)
def number_route(n):
    """Route number/<n>"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>/', strict_slashes=False)
def number_template(n):
    """Route number_template/<n>"""
    n = str(n)
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
