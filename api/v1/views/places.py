#!/usr/bin/python3
"""A new view for place objects that handles all default RESTful actions"""


from flask import abort, request, jsonify
from models import storage, Place, User, City
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def list_places(city_id):
    """Function that retrive all places"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    places = [place.to_dict() for place in city.places]
    return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def single_place(place_id):
    """Function that retrive a single place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """Function that delete a place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    place.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def add_place(city_id):
    """Fundtion that add a places"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    user_id = data.get('user_id')
    if not user_id:
        abort(400, 'Missing user_id')
    user = storage.get(User, user_id)
    if not user:
        abort(400, 'User Not Found')
    name = data.get('name')
    if not name:
        abort(400, 'Missing name')
    data['city_id'] = city_id
    place = Place(**data)
    place.save()
    return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """Function that update a place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    keys = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
    for key, value in data.item():
        if key not in keys:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def search_places():
    """Function that search for a list of places in the storage"""
    try:
        request_data = request.get_json()
    except Exception:
        abort(400, 'Not a JSON')
    if not request_data:
        list_place = [place.to_dict() for place in storage.all('Place').values()]
        return jsonify(list_place)
    states = request_data.get('states', [])
    cities = request_data.get('cities', [])
    amenities = request_data.get('amenities', [])
    if not states and not cities and not amenities:
        list_place = [place.to_dict() for place in storage.all('Place').values()]
        return jsonify(list_place)
    all_places = storage.all('Place').values()
    list_place = []
    for place in all_places:
        if 'Place' in place.__class__.__name__:
            if place.state_id in states or place.city_id in cities:
                list_place.append(place)
    if amenities:
        filtered_places = []
        for place in list_place:
            if all(amenity in [a.id for a in place.amenities] for amenity in amenities):
                filtered_place.append(place)
        list_place = filtered_place
    return jsonify([place.to_dict() for place in list_place])
