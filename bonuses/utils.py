from flask import g, current_app
from flask_pymongo import PyMongo


def get_mongo():
    if not hasattr(g, 'mongo_connection'):
        g.mongo_connection = PyMongo(current_app)
    return g.mongo_connection
