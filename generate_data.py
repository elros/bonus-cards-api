import os
import random
from datetime import datetime, timedelta


os.environ['BONUSES_API_SETTINGS'] = os.path.join(os.path.dirname(__file__), 'settings.py')

from bonuses.app import bonuses_app, bcrypt, mongo


LOCATIONS = [
    'KRR',
    'DME',
    'SVO',
    'LED',
]


def main():
    with bonuses_app.app_context():
        delete_objects()
        create_users()
        create_random_transactions()


def delete_objects():
    mongo.db.users.delete_many({})
    mongo.db.transactions.delete_many({})


def create_users():
    mongo.db.users.insert_many([
        {
            'username': 'alice',
            'pwd_hash': bcrypt.generate_password_hash('alice_secret'),
            'full_name': 'Alice Doe',
            'email': 'alice@localhost',
            'bonus_card_id': '000001',
        },
        {
            'username': 'bob',
            'pwd_hash': bcrypt.generate_password_hash('bob_secret'),
            'full_name': 'Bob Doe',
            'email': 'bob@localhost',
            'bonus_card_id': '000002',
        },
    ])


def create_random_transactions(count=42):
    users = list(mongo.db.users.find())
    for _ in range(count):
        create_transaction(user=random.choice(users))


def create_transaction(user):
    with bonuses_app.app_context():
        mongo.db.transactions.insert_one({
            'bonus_card_id': user['bonus_card_id'],
            'points': random.randint(1, 100),
            'flight_from': random.choice(LOCATIONS),
            'flight_to': random.choice(LOCATIONS),
            'flight_date': (datetime.now() + timedelta(days=random.randint(-30, 0)))
        })


if __name__ == '__main__':
    main()
