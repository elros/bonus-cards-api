from flask import Flask

from bonuses.database import mongo
from bonuses.api import (client, third_party)


app = Flask('bonuses_api')
app.config.from_envvar('BONUSES_API_SETTINGS')
mongo.init_app(app)

api_prefix = app.config['BONUSES_API_PREFIX']

app.register_blueprint(client.api, url_prefix=(api_prefix + '/client'))
app.register_blueprint(third_party.api, url_prefix=(api_prefix + '/third-party'))
