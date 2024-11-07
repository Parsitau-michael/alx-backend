#!/usr/bin/env python3
"""
This module sets up a basic Flask app
"""


from flask import Flask, request, g, render_template
from flask_babel import Babel
from pytz import timezone, utc, UnknownTimeZoneError


class Config:
    """
    A class to configure available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from the Config class

babel = Babel(app)  # Initialize Babel with the Flask app


def get_user():
    """
    A function that returns a user dictionary or None if the ID cannot be
    found or if login_as was not passed.
    """
    # Get the user ID from the 'login_as' query parameter
    user_id = request.args.get('login_as')

    # Check if user_id is provided and if it exists in the users dictionary
    if user_id and int(user_id) in users:
        return users[int(user_id)]

    # Return None otherwise
    return None


@babel.timezoneselector
def get_timezone():
    """
    A function that gets the appropriate timezone
    """
    # 1. Check for timezone in the URL query parameters
    url_param_tz = request.args.get('timezone')
    if url_param_tz:
        try:
            return timezone(url_param_tz)
        except UnknownTimeZoneError:
            pass

    # 2. Check if the user is logged in and has a valid timezone set
    if g.user and g.user['timezone']:
        try:
            return timezone(g.user['timezone'])
        except UnknownTimeZoneError:
            pass

    # 3. Fallback to UTC if no timezone is found
    return utc


@app.before_request
def before_request():
    """
    A function that is executed before all other functions.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    A function to detect if the incoming request contains locale argument
    and ifs value is a supported locale, return it.
    If not or if the parameter is not present, determine the users best
    locale match with our supported languages.
    """
    # 1. Check for locale in the URL query parameters
    url_param_locale = request.args.get('locale')
    if url_param_locale:
        return url_param_locale

    # 2. Check if the user is logged in and has a valid locale set
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Check the Accept-Language header from the request
    req_header_locale = request.headers.get('Accept-Language')
    if req_header_locale:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    # 4. Fallback to the default locale if nothing is found
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """
    A function defining the route
    """
    return render_template('7777777-index.html', user=g.user)


if __name__ == "__main__":
    app.run()
