from collections import namedtuple

from flask_pymongo import PyMongo


mongo = PyMongo()


User = namedtuple('User', (
    'id',
    'username',
    'pwd_hash',
    'full_name',
    'email',
    'bonus_card_id',
))
BonusCard = namedtuple('BonusCard', (
    'id',
))
BonusTransaction = namedtuple('BonusTransaction', (
    'id',
    'bonus_card_id',
    'points',
    'flight_from',
    'flight_to',
    'flight_date',
))


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
    convert = lambda val: val if type(val) in (str, bytes) else str(val)
    return User(
        id=convert(user['_id']),
        username=convert(user['username']),
        pwd_hash=convert(user['pwd_hash']),
        full_name=convert(user['full_name']),
        email=convert(user['email']),
        bonus_card_id=convert(user['bonus_card_id']),
    )
