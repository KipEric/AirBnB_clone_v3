#!/usr/bin/python3
"""A new view of State objects that handles all defaul RESTful actions"""


from flask import Flask, abort, request, jsonify
from api.v1.views import app_views
from os import name
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def list_all_states():
    """Function that retrive all states objects"""
    states = storage.all(State).values()
    all_states = [state.to_dict() for state in states]
    return jsonify(all_states)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashe=False)
def single_state(state_id):
    """Function that retrive  a single state object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Function that create new state"""
    data = request.get_json()
    if not data:
        abort(400,'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Function that delete state using state id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Function that update the state objects"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for i, j in data.items():
        if i not in ['id', 'created_at', 'updated_at']:
            setattr(state, i, j)
    state.save()
    return jsonify(state.to_dict()), 200
