#!/usr/bin/python3
"""api that calls close function"""


from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def downtear(self):
    """function that return close"""
    storage.close()
