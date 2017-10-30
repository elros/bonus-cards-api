from flask import Blueprint, jsonify, current_app, request
from flask_jwt import jwt_required, current_identity

from bonuses.database import get_transactions_by_bonus_card_id
from bonuses.utils import get_paginated_part


api = Blueprint('client_api', __name__)


@api.route('/profile')
@jwt_required()
def get_profile():
    return jsonify({
        'full_name': current_identity.full_name,
        'email': current_identity.email,
        'bonus_card_id': current_identity.bonus_card_id,
    })


@api.route('/bonus-transactions/')
@jwt_required()
def get_bonus_transactions_list():
    transactions = [{
        'bonus_card_id': str(transaction.bonus_card_id),
        'points': int(transaction.points),
        'flight_from': str(transaction.flight_from),
        'flight_to': str(transaction.flight_to),
        'flight_date': transaction.flight_date
    } for transaction in get_transactions_by_bonus_card_id(current_identity.bonus_card_id)]

    return jsonify({
        'transactions': get_paginated_part(
            items=transactions,
            page=int(request.values.get('page', 1)),
            page_size=current_app.config['TRANSACTIONS_LIST_PAGE_SIZE'],
        )
    })
