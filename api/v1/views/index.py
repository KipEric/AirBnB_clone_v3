#!/usr/bin/python3
"""Status of the API"""

import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views



@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Method that return status of the api"""
    if request.method == 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)


@app_views.route('/api/v1/stats', strict_slashes=False)
def stat():
    """Function that retrieves the number of each objects by type"""
    if request.method == 'GET':
        response = {}
    elem = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "State": "states",
        "Review": "reviews",
        "User": "users"
    }
    for key, value in elem.items():
        response[value] = storage.count(key)
    return jsonify(response)
