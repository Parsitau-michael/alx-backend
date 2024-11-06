#!/usr/bin/env python3
"""
A module that starts a Basic Flask app
"""


from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    """
    A function to describe the route
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
