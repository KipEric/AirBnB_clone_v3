#!/usr/bin/python3
"""Flask script"""


from flask import Flask, jsonify, make_response, render_template, url_for
from models import storage
from os import getenv
from api.v1.views import app_views
from flask_cors import CORS, cross_origin
from flasgger import Swagger
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
swagger = Swagger(app)
app.register_blueprint(app_views)
app.url_mao.strict_slashes=False
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def tear_down(exception):
    """API status"""
    storage.close()


@app.errorhandler(404)
def page_not_found(exception):
    """Function to handle error code 404"""
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
