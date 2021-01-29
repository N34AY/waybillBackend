from flask import Blueprint, render_template, request, jsonify, redirect, make_response, url_for


from application.companies.models import Company


mod_companies = Blueprint('auth', __name__, url_prefix='/companies')


@mod_companies.route('create', methods=['GET', 'POST'])
def create_company_page():
    if request.method == 'POST':
        company_name = request.form.get('company_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        description = request.form.get('description')

        company = {'company_name': company_name, 'phone': phone, 'email': email, 'description': description}
        Company.insert_one(company)
        return render_template('companies/create.html', message="Компания успешно создана!")
    if request.method == 'GET':
        return render_template('companies/create.html')
