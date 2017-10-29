from werkzeug.exceptions import Unauthorized
from flask_jwt import JWT
from flask_bcrypt import Bcrypt

from bonuses.database import get_user_by_username, get_user_by_id
from bonuses.utils import make_bruteforce_ip_filter


jwt = JWT()
bcrypt = Bcrypt()


bruteforce_filter = make_bruteforce_ip_filter(
    window_cfg='BRUTEFORCE_WINDOW',
    threshold_cfg='BRUTEFORCE_THRESHOLD',
    lag_cfg='BRUTEFORCE_LAG'
)


@bruteforce_filter
def authenticate(username, password):
    user = get_user_by_username(username)

    if not user or not bcrypt.check_password_hash(user.pwd_hash, password.encode('utf-8')):
        raise Unauthorized

    return user


def identity(payload):
    user_id = payload['identity']
    user = get_user_by_id(user_id)

    if not user:
        raise Unauthorized

    return user


jwt.authentication_handler(authenticate)
jwt.identity_handler(identity)
