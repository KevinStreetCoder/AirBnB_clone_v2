#!/usr/bin/python3
"""
This script starts a Flask web application with multiple routes.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that displays 'Hello HBNB!' on the root URL.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that displays 'HBNB' on the '/hbnb' URL.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route that displays 'C ' followed by the value of the text variable
    with underscores (_) replaced by spaces.
    """
    return "C " + text.replace("_", " ")

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_route(text="is cool"):
    """
    Route that displays 'Python ' followed by the value of the text variable
    with underscores (_) replaced by spaces. The default value of text is "is cool."
    """
    return "Python " + text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Route that displays 'n is a number' if n is an integer.
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
