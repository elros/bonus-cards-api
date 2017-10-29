from collections import namedtuple

from werkzeug.exceptions import Unauthorized
from flask_jwt import JWT
from flask_pymongo import ObjectId

from bonuses.database import mongo
from bonuses.utils import make_bruteforce_ip_filter


jwt = JWT()


User = namedtuple('User', 'id username')


bruteforce_filter = make_bruteforce_ip_filter(
    window_cfg='BRUTEFORCE_WINDOW',
    threshold_cfg='BRUTEFORCE_THRESHOLD',
    lag_cfg='BRUTEFORCE_LAG'
)


@bruteforce_filter
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
