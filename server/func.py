import datetime
import dbm

from config import *
from collections import OrderedDict


def get_pg_data():
    date = datetime.datetime.now().date().isoformat()
    time = datetime.datetime.now().time().isoformat()[:8:]
    dt = date + ' ' + time

    return dt


def get_all_sub_specs(id_spec, sub_specs):
    list_of_specs = {}

    for spec in sub_specs:
        if spec[2] and not spec[3] and spec[4] and spec[5] is None:
            db.execute('SELECT param_name FROM params WHERE id_param = %s', [spec[2]])
            param_name = db.fetchone()[0]
            list_of_specs[param_name] = spec[4]
            continue
        if spec[2] and spec[3] and spec[4] is None and spec[5] is None:
            db.execute('SELECT param_name FROM params WHERE id_param = %s', [spec[2]])
            param_name = db.fetchone()[0]
            db.execute('SELECT val FROM pot_value WHERE id_param = %s and id_value = %s and id_spec = %s', [spec[2], spec[3], id_spec])
            pot_value = db.fetchone()[0]
            list_of_specs[param_name] = pot_value
            continue
        if spec[2] and spec[3] is None and spec[4] is None and spec[5]:
            db.execute('SELECT param_name FROM params WHERE id_param = %s', [spec[2]])
            param_name = db.fetchone()[0]
            id_sprav = spec[5]
            id_object = spec[6]
            db.execute('SELECT table_name FROM sprav_objects WHERE id_object = %s', [id_sprav])
            table_name = db.fetchone()[0]
            list_of_specs[param_name] = get_all_specs(table_name, id_object)
            continue
        if spec[2] and spec[3] is None and spec[4] is None and spec[5] is None:
            db.execute('SELECT param_name FROM params WHERE id_param = %s', [spec[2]])
            param_name = db.fetchone()[0]
            sub_specs = get_all_sub_specs(spec[0], sub_specs)
            list_of_specs[param_name] = sub_specs
            continue
    #print(list_of_specs)
    return list_of_specs


def get_all_specs(name_tb, id_obj):
    list_of_specs = {}

    dt = get_pg_data()

    if name_tb == 'individ':
        db.execute(f'SELECT id_individ, fam, name, otch, data_rogd from individ where id_individ=%s', [id_obj])
        individ = db.fetchone()
        list_of_specs["ID"] = individ[0]
        list_of_specs["Фамилия"] = individ[1]
        list_of_specs["Имя"] = individ[2]
        list_of_specs["Отчество"] = individ[3]
        list_of_specs["Дата_рождения"] = individ[4]
        db.execute('SELECT * FROM individ_specs WHERE id_individ = %s and '
                   '((date_from < %s and date_to is null) or (date_from < %s and date_to > %s )) ORDER BY id_spec',
                   [id_obj, dt, dt, dt])

    if name_tb == 'organization':
        db.execute(f'SELECT id_org, full_name, short_name, inn, kpp, ogrn FROM organization where id_org=%s', [id_obj])
        organization = db.fetchone()
        list_of_specs["ID"] = organization[0]
        list_of_specs["Полное_имя"] = organization[1]
        list_of_specs["Корот_имя"] = organization[2]
        list_of_specs["ИНН"] = organization[3]
        list_of_specs["КПП"] = organization[4]
        list_of_specs["ОРГН"] = organization[5]
        db.execute('SELECT * FROM organization_specs WHERE id_organization = %s and '
                   '((date_from < %s and date_to is null) or (date_from < %s and date_to > %s )) ORDER BY id_spec',
                   [id_obj, dt, dt, dt])

    if name_tb == 'tko':
        db.execute(f'SELECT id_tko, is_dynamic FROM tko where id_tko=%s', [id_obj])
        tko = db.fetchone()
        list_of_specs["ID"] = tko[0]
        list_of_specs["Передвижной"] = tko[1]
        db.execute('SELECT * FROM tko_specs WHERE id_tko = %s and '
                   '((date_from < %s and date_to is null) or (date_from < %s and date_to > %s )) ORDER BY id_spec',
                   [id_obj, dt, dt, dt])

    specs = db.fetchall()
    child_specs = []

    for child in specs:
        if not child[8] is None:
            child_specs.append(child)

    for child in child_specs:
        if child in specs:
            specs.remove(child)

    for spec in specs:
        if spec[2] and not spec[3] and spec[4] and spec[5] is None and spec[8] is None:
            db.execute('SELECT param_name FROM params WHERE id_param = %s', [spec[2]])
            param_name = db.fetchone()[0]
            list_of_specs[param_name] = spec[4]
            continue
        if spec[2] and spec[3] and spec[4] is None and spec[5] is None and spec[8] is None:
            db.execute('SELECT param_name FROM params WHERE id_param = %s', [spec[2]])
            param_name = db.fetchone()[0]
            db.execute('SELECT val FROM pot_value WHERE id_param = %s and id_value = %s', [spec[2], spec[3]])
            pot_value = db.fetchone()[0]
            list_of_specs[param_name] = pot_value
            continue
        if spec[2] and spec[3] is None and spec[4] is None and spec[5] and spec[8] is None:
            db.execute('SELECT param_name FROM params WHERE id_param = %s', [spec[2]])
            param_name = db.fetchone()[0]
            id_sprav = spec[5]
            id_object = spec[6]
            db.execute('SELECT table_name FROM sprav_objects WHERE id_object = %s', [id_sprav])
            table_name = db.fetchone()[0]
            list_of_specs[param_name] = get_all_specs(table_name, id_object)
            continue
        if spec[2] and spec[3] is None and spec[4] is None and spec[5] is None:
            db.execute('SELECT param_name FROM params WHERE id_param = %s', [spec[2]])
            param_name = db.fetchone()[0]
            sub_specs = get_all_sub_specs(spec[0], child_specs)
            list_of_specs[param_name] = sub_specs
            continue

    return list_of_specs
