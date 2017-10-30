from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required

from bonuses.database import BonusTransaction, create_bonus_transaction
from bonuses.utils import parse_iso8601_date


api = Blueprint('third_party_api', __name__)


@api.route('/bonus-transactions/', methods=['POST'])
@jwt_required()
def add_user_bonus_transaction():
    created_id = create_bonus_transaction(BonusTransaction(
        id=None,
        bonus_card_id=request.json['bonus_card_id'],
        points=int(request.json['points']),
        flight_from=request.json['flight_from'],
        flight_to=request.json['flight_to'],
        flight_date=parse_iso8601_date(request.json['flight_date']),
    ))
    return jsonify({'success': True, 'id': created_id})
