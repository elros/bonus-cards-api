from flask import Blueprint, jsonify


api = Blueprint('third_party_api', __name__)


@api.route('/bonus-transactions/<int:user_id>/', methods=['POST'])
def add_user_bonus_transaction(user_id):
    return jsonify({'todo': True})
