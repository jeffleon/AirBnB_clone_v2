#!/usr/bin/python3
"""Module for start Flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """" return a hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbhb():
    """" return HBNB """
    return "HBNB"


@app.route('/c/<text>')
def definetext(text):
    """ return c + text that you type """
    text = text.replace('_', '')
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def defintectpython(text="is cool"):
    """ return python + that you type """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
