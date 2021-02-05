from datetime import datetime
from bson import ObjectId


from flask import Blueprint, request


from application.companies.models import Company
from application.lists.models import List


mod_lists = Blueprint('lists', __name__, url_prefix='/lists')


@mod_lists.route('/create', methods=['POST'])
def create_list():
    name = request.json.get('name')
    company_id = request.json.get('company')
    company = Company.find_one({'_id': ObjectId(oid=company_id)})

    new_list = {'name': name, 'company': company, "created_at": datetime.utcnow(), "updated_at": None}
    List.insert_one(new_list)

    return {"status": "success"}


@mod_lists.route('/get/<ObjectId:list_id>', methods=['GET'])
def get_list(list_id):
    lst = List.find_one({'_id': ObjectId(oid=list_id)})

    company = {"id": str(lst['company']['_id']), "name": lst['company']['name']}
    lst = {"id": str(lst['_id']), "name": lst['name'], "company": company}

    return {"status": "success", "list": lst}


@mod_lists.route('edit/<ObjectId:list_id>', methods=['POST'])
def edit_list(list_id):
    name = request.json.get('name')
    company_id = request.json.get('company')

    company = Company.find_one({'_id': ObjectId(oid=company_id)})

    lst = {"$set": {'name': name, 'company': company, "updated_at": datetime.utcnow()}}
    List.update_one({'_id': ObjectId(oid=list_id)}, lst)

    return {"status": "success"}


@mod_lists.route('delete/<ObjectId:list_id>', methods=['DELETE'])
def delete_list(list_id):
    List.delete_one({'_id': ObjectId(oid=list_id)})

    return {"status": "success"}


@mod_lists.route('/', methods=['GET'])
def all_lists():
    lists = []
    for lst in List.find():
        list_obj = {"id": str(lst['_id']), "name": lst['name'], "company": lst['company']['name'], "created_at": lst['created_at'], "updated_at": lst['updated_at']}
        lists.append(list_obj)

    return {"status": "success", "lists": lists}
