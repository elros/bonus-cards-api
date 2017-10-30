from collections import namedtuple

from flask_pymongo import PyMongo, ObjectId


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


def db_str(val):
    if type(val) in (str, bytes):
        return val
    else:
        return str(val)


def get_user_by_username(username):
    user = mongo.db.users.find_one({'username': username})
    if user is None:
        return None
    else:
        return mongo_user_to_namedtuple(user)


def mongo_user_to_namedtuple(user):
    return User(
        id=db_str(user['_id']),
        username=db_str(user['username']),
        pwd_hash=db_str(user['pwd_hash']),
        full_name=db_str(user['full_name']),
        email=db_str(user['email']),
        bonus_card_id=db_str(user['bonus_card_id']),
    )


def get_user_by_id(user_id):
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if user is None:
        return None
    else:
        return mongo_user_to_namedtuple(user)


def get_transactions_by_bonus_card_id(bonus_card_id):
    transactions = mongo.db.transactions.find({'bonus_card_id': bonus_card_id})
    return [
        BonusTransaction(
            id=db_str(transaction['_id']),
            bonus_card_id=db_str(transaction['bonus_card_id']),
            points=int(transaction['points']),
            flight_from=db_str(transaction['flight_from']),
            flight_to=db_str(transaction['flight_to']),
            flight_date=db_str(transaction['flight_date']),
        )
        for transaction in transactions
    ]


def create_bonus_transaction(bonus_transaction):
    if not isinstance(bonus_transaction, BonusTransaction):
        raise TypeError('Expecting argument bonus_transaction of type BonusTransaction')

    as_dict = bonus_transaction._asdict()
    del as_dict['id']

    created_object = mongo.db.transactions.insert_one({**as_dict})

    return str(created_object.inserted_id)
