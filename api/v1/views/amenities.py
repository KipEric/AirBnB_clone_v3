#!/usr/bin/python3
"""A new view for amenity objects that handles all RESTful API actions"""


from flask import request, jsonify, abort
from api.v1.views import app_views
from models import storage, Amenity
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def all_amenities():
    """Finction that retrive all amenities"""
    amenities = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for amenity in amenities])


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def single_amenity(amenity_id):
    """Function that retrive a single amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenit is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """Function that delete amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_view.route('/amenities', methods=['POST'], strict_slashes=False)
def add_amenity():
    """Function that add an amenity"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    data = request.get_json()
    amenity = Amenity(**data)
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201


@app_view.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """Function that update amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    data = request.get_json()
    ignore = ['id', 'created_at', 'updated_at']
    for i, j in data.items():
        if i not in ignore:
            setattr(amenity, i, j)
    storage.save()
    return jsonify(amenity.to_dict()), 200
