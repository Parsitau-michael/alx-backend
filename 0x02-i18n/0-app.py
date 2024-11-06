#!/usr/bin/env python3
"""
This module sets up a basic Flask app
"""


from flask import Flask, request, render_template
from flask_babel import Babel


class Config:
    """
    A class to configure available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config) # Load configuration from the Config class

babel =Babel(app) # Initialize Babel with the Flask app


@babel.localeselector
def get_locale():
    """
    A function to determine the users best locale match with our
    supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    A function defining the route
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
