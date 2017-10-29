from flask import Flask

from bonuses.database import mongo
from bonuses.auth import jwt, bcrypt
from bonuses.api import client, third_party


bonuses_app = Flask('bonuses_api')
bonuses_app.config.from_envvar('BONUSES_API_SETTINGS')

mongo.init_app(bonuses_app)
jwt.init_app(bonuses_app)
bcrypt.init_app(bonuses_app)

api_prefix = bonuses_app.config['BONUSES_API_PREFIX']

bonuses_app.register_blueprint(client.api, url_prefix=(api_prefix + '/client'))
bonuses_app.register_blueprint(third_party.api, url_prefix=(api_prefix + '/third-party'))
