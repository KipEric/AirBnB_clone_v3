#!/usr/bin/python3
"""New view for city objects that handles all default RESTful API actions"""


from flask import request, abort, jsonify
from api.v1.views import api_views
from models import storage, State, City


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def cities_by_state(state_id):
    """Function that retreves all cities in a state"""
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def single_city(city_id):
    """Function that retrive single city using its id"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Function that delete a city"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def add_city(state_id):
    """Function that add a city to a state"""
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    data = request.get_json()
    data['state_id'] = state_id
    city = City(**data)
    storage.new(city)
    storage.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Function that updates city"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    data = request.get_json()
    keys = ['id', 'state_id', 'created_at', 'updated_at']
    for i, j in data.items():
        if i not in keys:
            setattr(city, i, j)
    storage.save()
    return jsonify(city.to_dict()), 200
