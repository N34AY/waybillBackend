from datetime import datetime
from bson import ObjectId


from flask import Blueprint, render_template, request, jsonify, redirect, make_response, url_for


from application.companies.models import Company
from application.lists.models import List


mod_lists = Blueprint('lists', __name__, url_prefix='/lists')


@mod_lists.route('create', methods=['GET', 'POST'])
def create_list():
    if request.method == 'POST':
        name = request.form.get('name')
        company_id = request.form.get('company')
        company = Company.find_one({'_id': ObjectId(oid=company_id)})

        new_list = {'name': name, 'company': company, "created_at": datetime.utcnow(), "updated_at": None}
        List.insert_one(new_list)

        return redirect(url_for('lists.all_lists'))
    if request.method == 'GET':
        companies = []
        for company in Company.find():
            company_obj = {"id": str(company['_id']), "name": company['name']}
            companies.append(company_obj)

        return render_template('lists/create.html', companies=companies)


@mod_lists.route('edit/<ObjectId:list_id>', methods=['GET', 'POST'])
def edit_list(list_id):
    if request.method == 'POST':
        name = request.form.get('name')
        company_id = request.form.get('company')
        print(company_id)
        company = Company.find_one({'_id': ObjectId(oid=company_id)})

        lst = {"$set": {'name': name, 'company': company, "updated_at": datetime.utcnow()}}
        List.update_one({'_id': ObjectId(oid=list_id)}, lst)

        return redirect(url_for('lists.all_lists'))
    if request.method == 'GET':
        companies = []
        for company in Company.find():
            company_obj = {"id": str(company['_id']), "name": company['name']}
            companies.append(company_obj)

        lst = List.find_one({'_id': ObjectId(oid=list_id)})
        return render_template('lists/edit.html', lst=lst, companies=companies)


@mod_lists.route('delete/<ObjectId:list_id>', methods=['GET'])
def delete_list(list_id):
    List.delete_one({'_id': ObjectId(oid=list_id)})
    return redirect(url_for('lists.all_lists'))


@mod_lists.route('/', methods=['GET'])
def all_lists():
    lists = []
    for lst in List.find():
        list_obj = {"id": str(lst['_id']), "name": lst['name'], "company": lst['company']['name'], "created_at": lst['created_at'], "updated_at": lst['updated_at']}
        lists.append(list_obj)
    return render_template('lists/all.html', lists=lists)
