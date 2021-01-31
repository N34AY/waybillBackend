from datetime import datetime
from bson import ObjectId


from flask import Blueprint, render_template, request, jsonify, redirect, make_response, url_for


from application.companies.models import Company
from application.lists.models import List
from application.waybill.models import Waybill


mod_waybills = Blueprint('waybills', __name__, url_prefix='/waybills')


@mod_waybills.route('create', methods=['GET', 'POST'])
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
