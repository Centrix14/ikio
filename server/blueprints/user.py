from flask import Blueprint, jsonify, request
from func import *

user_bp = Blueprint('user_bp', __name__)

"""
TO DO 
Добавить в регистрацию заполнение параметров
"""


@user_bp.route('/register', methods=['POST'])
def register():
    post_data = request.get_json()
    fam = post_data.get("fam")
    name = post_data.get("name")
    otch = post_data.get("otch")
    data_rogd = post_data.get("data_rogd")
    login = post_data.get("login")
    password = post_data.get("password")

    db.execute('SELECT max(id_individ) from individ')
    max_id = db.fetchone()[0]

    if max_id is None:
        max_id = 0

    max_id += 1

    date_from = get_pg_data()

    db.execute('INSERT INTO individ (id_individ, fam, name, otch, data_rogd) VALUES (%s, %s, %s, %s)',
               [max_id, fam, name, otch, data_rogd])

    db.execute('INSERT INTO individ_specs (id_spec, id_individ, id_param, value_tut, date_from) VALUES (%s, '
               '%s, %s, %s, %s)', [1, max_id, 33, login, date_from])

    db.execute('INSERT INTO individ_specs (id_spec, id_individ, id_param, value_tut, date_from) VALUES (%s, '
               '%s, %s, %s, %s)', [2, max_id, 34, password, date_from])

    response = {
        "status": True
    }

    return jsonify(response)


@user_bp.route('/login', methods=['POST'])
def login():
    post_data = request.get_json()
    login = post_data.get("login")
    password = post_data.get("password")

    db.execute('SELECT id_individ from individ_specs where value_tut = %s and id_param=33', (login,))
    exists_login = db.fetchone()[0]
    if exists_login is None:
        return jsonify({
            "message": "Неверный логин или пароль",
            "status": False
        })

    db.execute('SELECT id_individ from individ_specs where value_tut = %s and id_param=34', (password,))
    exists_password = db.fetchone()[0]
    if exists_password is None:
        return jsonify({
            "message": "Неверный логин или пароль",
            "status": False
        })

    id_individ = exists_password

    response = {"data": get_all_specs('individ', id_individ), "message": "Успешно!", "status": True}
    return jsonify(response)


@user_bp.route('/get_all_users', methods=['GET'])
def get_all_users():
    db.execute('SELECT max(id_individ) FROM individ')
    max_id = db.fetchone()[0]
    if max_id is None:
        return {
            'message': 'Пользователей нет',
            "status": False
        }

    data = []

    for i in range(1, max_id+1):
        data.append(get_all_specs('individ', i))

    response = {"data": data, "message": "Успешно!", "status": True}
    return jsonify(response)
