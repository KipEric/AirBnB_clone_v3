#!/usr/bin/python3
"""A new view for user object that handles all defaulth RESTful API actions"""


from flask import request, jsonify, abort
from models import storage
from api.v1.views import app_views
from models.user import Users


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def all_users():
    """Function that retrive all users"""
    users = storage.all(User).values()
    list_users = [user.to_dict() for user in users]
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def single_user(user_id):
    """Function that retrive a single user"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def add_user():
    """Function that add a user"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'email' not in data:
        abort(400, 'Missing email')
    if 'password' not in data:
        abort(400, 'Missing password')
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Function that delete a user"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({})


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Function that update a user"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    keys = ['id', 'email', 'created_at', 'updated_at']
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    for i, j in data.items():
        if i not in keys:
            setattr(user, i, j)
    user.save()
    return jsonify(user.to_dict())
