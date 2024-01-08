from flask import Blueprint, jsonify, request
from func import *

organization_bp = Blueprint('organization_bp', __name__)

"""
TO DO
Добавить добавление организации, если дойдет
"""

@organization_bp.route('/get_one_organization', methods=['GET'])
def get_one_organization():
    post_data = request.get_json()
    id_org = post_data.get("id")

    response = {"data": get_all_specs('organization', id_org), "message": "Успешно!", "status": True}
    return jsonify(response)


@organization_bp.route('/get_all_organizations', methods=['GET'])
def get_all_organizations():
    db.execute('SELECT max(id_org) FROM organization')
    max_id = db.fetchone()[0]
    if max_id is None:
        return {
            'message': 'Организаций нет',
            "status": False
        }

    data = []

    for i in range(1, max_id+1):
        data.append(get_all_specs('organization', i))

    response = {"data": data, "message": "Успешно!", "status": True}
    return jsonify(response)
