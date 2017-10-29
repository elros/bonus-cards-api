from flask import Blueprint, jsonify, current_app
from flask_jwt import jwt_required, current_identity


api = Blueprint('client_api', __name__)


@api.route('/profile')
@jwt_required()
def get_profile():
    return jsonify({'todo': True, 'id': str(current_identity)})


@api.route('/bonus-transactions/')
@jwt_required()
def get_bonus_transactions_list():
    return jsonify({'todo': True})
