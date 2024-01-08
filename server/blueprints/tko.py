from flask import Blueprint, jsonify, request
from func import *

tko_bp = Blueprint('tko_bp', __name__)

"""
TO DO
Добавить добавление организации, если дойдет
"""


@tko_bp.route('/get_one_tko', methods=['GET'])
def get_one_tko():
    post_data = request.get_json()
    id_tko = post_data.get("id")

    response = {"data": get_all_specs('tko', id_tko), "message": "Успешно!", "status": True}
    return jsonify(response)


@tko_bp.route('/get_all_tko', methods=['GET'])
def get_all_tko():
    db.execute('SELECT max(id_tko) FROM tko')
    max_id = db.fetchone()[0]
    if max_id is None:
        return {
            'message': 'ТКО нет',
            "status": False
        }

    data = []

    for i in range(1, max_id+1):
        data.append(get_all_specs('tko', i))
        print(data)

    response = {"data": data, "message": "Успешно!", "status": True}
    return jsonify(response)
