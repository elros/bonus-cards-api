from collections import namedtuple

from werkzeug.exceptions import Unauthorized
from flask_jwt import JWT
from flask_pymongo import ObjectId

from bonuses.database import mongo


jwt = JWT()


User = namedtuple('User', 'id username')


def authenticate(username, password):
    user = mongo.db.users.find_one({'username': username})

    if not user or user['password'] != password:
        raise Unauthorized

    return User(
        id=str(user['_id']),
        username=username
    )


def identity(payload):
    user_id = payload['identity']
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})

    if not user:
        raise Unauthorized

    return User(
        id=str(user['_id']),
        username=str(user['username'])
    )


jwt.authentication_handler(authenticate)
jwt.identity_handler(identity)
