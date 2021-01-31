from datetime import datetime
from bson import ObjectId


from flask import Blueprint, render_template, request, jsonify, redirect, make_response, url_for


from application.companies.models import Company


mod_companies = Blueprint('companies', __name__, url_prefix='/companies')


@mod_companies.route('create', methods=['GET', 'POST'])
def create_company():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        description = request.form.get('description')

        company = {'name': name, 'phone': phone, 'email': email, 'description': description, "created_at": datetime.utcnow()}
        Company.insert_one(company)

        return redirect(url_for('companies.all_companies'))
    if request.method == 'GET':
        return render_template('companies/create.html')


@mod_companies.route('edit/<ObjectId:company_id>', methods=['GET', 'POST'])
def edit_company(company_id):
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        description = request.form.get('description')

        company = {"$set": {'name': name, 'phone': phone, 'email': email, 'description': description, "updated_at": datetime.utcnow()}}
        Company.update_one({'_id': ObjectId(oid=company_id)}, company)

        return redirect(url_for('companies.all_companies'))
    if request.method == 'GET':
        company = Company.find_one({'_id': ObjectId(oid=company_id)})
        return render_template('companies/edit.html', company=company)


@mod_companies.route('delete/<ObjectId:company_id>', methods=['GET'])
def delete_company(company_id):
    Company.delete_one({'_id': ObjectId(oid=company_id)})
    return redirect(url_for('companies.all_companies'))


@mod_companies.route('/', methods=['GET'])
def all_companies():
    companies = []
    for company in Company.find():
        company_obj = {"id": str(company['_id']), "name": company['name'], "phone": company['phone'], "email": company['email'], 'description': company['description']}
        companies.append(company_obj)
    return render_template('companies/all.html', companies=companies)
