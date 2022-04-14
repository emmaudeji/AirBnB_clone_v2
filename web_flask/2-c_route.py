#!/usr/bin/python3
<<<<<<< HEAD
"""
starts a Flask web application
"""

from flask import Flask
=======
"""Starts Flask web app
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
    /c/<text> - display "C <text>"
"""
from flask import Flask

>>>>>>> 9f586a63ae3ad74ef81f0be80be9a1005f832d7a
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'
=======
def hbnb_route():
    """prints Hello HBNB"""
    return "Hello HBNB!"
>>>>>>> 9f586a63ae3ad74ef81f0be80be9a1005f832d7a


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
    """prints HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """prints C followed by <text> content"""
    text = text.replace("_", " ")
    return "C %s" % text

if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> 9f586a63ae3ad74ef81f0be80be9a1005f832d7a
