from flask import Blueprint, jsonify, current_app
from flask_jwt import jwt_required, current_identity

from bonuses.utils import make_bruteforce_ip_filter


api = Blueprint('client_api', __name__)


bruteforce_filter = make_bruteforce_ip_filter(
    window_cfg='BRUTEFORCE_WINDOW',
    threshold_cfg='BRUTEFORCE_THRESHOLD',
    lag_cfg='BRUTEFORCE_LAG'
)


@api.route('/login', methods=['POST'])
@bruteforce_filter
def make_login():
    return jsonify({'todo': True})


@api.route('/profile')
@jwt_required()
def get_profile():
    return jsonify({'todo': True, 'id': str(current_identity)})


@api.route('/bonus-transactions/')
@jwt_required()
def get_bonus_transactions_list():
    return jsonify({'todo': True})
