#!/usr/bin/python3
"""
This script starts a Flask web application with multiple routes.
"""

from flask import Flask, render_template

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

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route that displays an HTML page with 'Number: n' if n is an integer.
    """
    return render_template('6-number_template.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route that displays an HTML page with 'Number: n is even|odd' if n is an integer.
    """
    if n % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    return render_template('6-number_odd_or_even.html', n=n, even_or_odd=even_or_odd)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

