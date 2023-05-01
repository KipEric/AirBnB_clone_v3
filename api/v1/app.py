#!/usr/bin/python3
"""Flask script"""


from flask import Flask, jsonify
from models import storage
from os import getenv
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teard(self):
    """API status"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Function to handle error code 404"""
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = 5000
    app.run(host=host, port=port, threaded=True)
