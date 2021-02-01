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
        data = request.form.get('data')
        lst_id = request.form.get('lst')
        lst = List.find_one({'_id': ObjectId(oid=lst_id)})

        new_waybill = {'name': name, 'lst': lst, "data": data, "created_at": datetime.utcnow(), "updated_at": None}
        Waybill.insert_one(new_waybill)

        return redirect(url_for('lists.all_lists'))
    if request.method == 'GET':
        lists = []
        for lst in List.find():
            lst_obj = {"id": str(lst['_id']), "name": lst['name'], "company": lst['company']}
            lists.append(lst_obj)
        table_data = [
            {
                "name": "name1",
                "article": "323432",
                "price": "284",
                "quantity": "10",
                "sum": "4"
            },
            {
                "name": "name2",
                "article": "32fgfd3432",
                "price": "24",
                "quantity": "20",
                "sum": "5343"
            }
        ]
        return render_template('waybills/create.html', lists=lists, table_data=table_data)
