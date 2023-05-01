#!/usr/bin/python3
"""Status of the API"""

import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def stts():
    """Method that return status of the api"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', strict_slashes=False)
def stat():
    """Function that retrieves the number of each objects by type"""
    elem = {
        'amenities': storage.count('models.Amenity'),
        'cities': storage.count('models.City'),
        'places': storage.count('models.Place'),
        'reviews': storage.count('models.Review'),
        'states': storage.count('models.State'),
        'users': storage.count('models.User')
    }
    return jsonify(elem)
