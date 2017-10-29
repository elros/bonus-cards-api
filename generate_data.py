import os


os.environ['BONUSES_API_SETTINGS'] = os.path.join(os.path.dirname(__file__), 'settings.py')

from bonuses.app import bonuses_app, bcrypt, mongo


def main():
    with bonuses_app.app_context():
        create_users()


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


if __name__ == '__main__':
    main()
