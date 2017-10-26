from flask import Blueprint, jsonify


api = Blueprint('client_api', __name__)


@api.route('/login', methods=['POST'])
def make_login():
    return jsonify({'todo': True})


@api.route('/profile')
def get_profile():
    return jsonify({'todo': True})


@api.route('/bonus-transactions/')
def get_bonus_transactions_list():
    return jsonify({'todo': True})
