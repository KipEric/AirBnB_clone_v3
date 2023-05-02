#!/usr/bin/python3
"""api that calls close function"""


from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def downtear(self):
    """function that return close"""
    storage.close()


@app.errorhandle(404)
def page_not_found(error):
    """Function to handle error code 404"""
    return jsonify({'error': 'Not found'}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = ''
