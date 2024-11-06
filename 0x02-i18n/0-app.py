#!/usr/bin/env python3
"""
This module sets up a basic Flask app
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    A function defining the route
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
