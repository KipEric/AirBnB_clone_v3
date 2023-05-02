#!/usr/bin/python3
"""initialization"""


from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.places import *
from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.users import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


app_views.register_blueprint(index)
app_views.register_blueprint(states)
app_views.register_blueprint(places)
app_views.register_blueprint(amenities)
app_views.register_blueprint(cities)
app_views.register_blueprint(users)
app_views.register_blueprint(places_reviews)
app_views.register_blueprint(places_amenities)
