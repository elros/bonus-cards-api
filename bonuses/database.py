from collections import namedtuple

from flask_pymongo import PyMongo


mongo = PyMongo()


User = namedtuple('User', 'id username pwd_hash full_name email bonus_card_id')


def get_user_by_username(username):
    user = mongo.db.users.find_one({'username': username})
    if user is None:
        return None
    else:
        return mongo_user_to_namedtuple(user)


def get_user_by_id(_id):
    user = mongo.db.users.find_one({'_id': _id})
    if user is None:
        return None
    else:
        return mongo_user_to_namedtuple(user)


def mongo_user_to_namedtuple(user):
    return User(
        id=str(user['_id']),
        username=str(user['username']),
        pwd_hash=str(user['pwd_hash']),
        full_name=str(user['full_name']),
        email=str(user['email']),
        bonus_card_id=str(user['bonus_card_id']),
    )
