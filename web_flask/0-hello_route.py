#!/usr/bin/python3

"""
This module contains a simple web application that greets the user with "Hello HBNB!"
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    Handles the root route and returns the greeting message
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
