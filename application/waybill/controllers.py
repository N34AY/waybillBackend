from datetime import datetime
from bson import ObjectId


from flask import Blueprint, render_template, request, jsonify, redirect, make_response, url_for


from application.companies.models import Company
from application.lists.models import List
from application.waybill.models import Waybill


mod_waybills = Blueprint('waybills', __name__, url_prefix='/waybills')


@mod_waybills.route('/create', methods=['POST'])
def create_waybill():
    name = request.json.get('name')
    sheet = request.json.get('sheet')
    lst_id = request.json.get('lst')

    lst = List.find_one({'_id': ObjectId(oid=lst_id)})

    new_waybill = {'name': name, 'lst': lst, "sheet": sheet, "created_at": datetime.utcnow(), "updated_at": None}
    Waybill.insert_one(new_waybill)

    return {"status": "success"}


@mod_waybills.route('/get/<ObjectId:waybill_id>', methods=['GET'])
def get_waybill(waybill_id):
    waybill = Waybill.find_one({'_id': ObjectId(oid=waybill_id)})

    lst = {"id": str(waybill['lst']['_id']), "name": waybill['lst']['name']}
    waybill = {"id": str(waybill['_id']), "name": waybill['name'], "lst": lst, "sheet": waybill['sheet']}

    return {"status": "success", "waybill": waybill}


@mod_waybills.route('edit/<ObjectId:waybill_id>', methods=['POST'])
def edit_list(waybill_id):
    name = request.json.get('name')
    lst_id = request.json.get('lst')
    sheet = request.json.get('sheet')

    lst = List.find_one({'_id': ObjectId(oid=lst_id)})

    waybill = {"$set": {"name": name, "lst": lst, "sheet": sheet, "updated_at": datetime.utcnow()}}
    Waybill.update_one({'_id': ObjectId(oid=waybill_id)}, waybill)

    return {"status": "success"}


@mod_waybills.route('delete/<ObjectId:waybill_id>', methods=['DELETE'])
def delete_list(waybill_id):
    Waybill.delete_one({'_id': ObjectId(oid=waybill_id)})

    return {"status": "success"}


@mod_waybills.route('/', methods=['GET'])
def all_waybills():
    waybills = []
    for waybill in Waybill.find():
        print(waybill)
        waybill_obj = {"id": str(waybill['_id']), "name": waybill['name'], "lst": waybill['lst']['name'], "created_at": waybill['created_at'], "updated_at": waybill['updated_at']}
        waybills.append(waybill_obj)

    return {"status": "success", "waybills": waybills}
