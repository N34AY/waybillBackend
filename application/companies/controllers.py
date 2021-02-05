from datetime import datetime
from bson import ObjectId


from flask import Blueprint, request

from application.companies.models import Company


mod_companies = Blueprint('companies', __name__, url_prefix='/companies')


@mod_companies.route('/create', methods=['POST'])
def create_company():
    if not request.data or not request.is_json:
        return {'status': 'error', 'message': ''}, 400

    name = request.json.get('name')
    phone = request.json.get('phone')
    email = request.json.get('email')
    description = request.json.get('description')

    company = {'name': name, 'phone': phone, 'email': email, 'description': description, "created_at": datetime.utcnow(), "updated_at": None}
    Company.insert_one(company)

    return {"status": "success"}, 200


@mod_companies.route('/get/<ObjectId:company_id>', methods=['GET'])
def get_company(company_id):
    company = Company.find_one({'_id': ObjectId(oid=company_id)})
    company = {"id": str(company['_id']), "name": company['name'], "phone": company['phone'],
               "email": company['email'], "description": company['description'],
               "created_at": company['created_at'], "updated_at": company['updated_at']}

    return {"status": "success", "company": company}, 200


@mod_companies.route('/edit/<ObjectId:company_id>', methods=['POST'])
def edit_company(company_id):
    name = request.json.get('name')
    phone = request.json.get('phone')
    email = request.json.get('email')
    description = request.json.get('description')

    company = {"$set": {'name': name, 'phone': phone, 'email': email,
                        'description': description, "updated_at": datetime.utcnow()}}
    Company.update_one({'_id': ObjectId(oid=company_id)}, company)

    return {"status": "success"}


@mod_companies.route('/delete/<ObjectId:company_id>', methods=['DELETE'])
def delete_company(company_id):
    Company.delete_one({'_id': ObjectId(oid=company_id)})

    return {"status": "success"}


@mod_companies.route('/', methods=['GET'])
def all_companies():
    companies = []
    for company in Company.find():
        company_obj = {"id": str(company['_id']), "name": company['name'], "phone": company['phone'],
                       "email": company['email'], 'description': company['description'],
                       "created_at": company['created_at'], "updated_at": company['updated_at']}
        companies.append(company_obj)

    return {"status": "success", "companies": companies}
