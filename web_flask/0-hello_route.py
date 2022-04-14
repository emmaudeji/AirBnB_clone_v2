#!/usr/bin/python3
<<<<<<< HEAD
"""
starts a Flask web application
=======
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes: /: Displays 'Hello HBNB!'
>>>>>>> 9f586a63ae3ad74ef81f0be80be9a1005f832d7a
"""

from flask import Flask
app = Flask(__name__)


<<<<<<< HEAD
@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> 9f586a63ae3ad74ef81f0be80be9a1005f832d7a
