from datetime import timedelta


from flask import Blueprint, request
from flask_jwt_extended import create_access_token


mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return {'status': 'error'}, 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return {'status': 'error'}, 400
    if not password:
        return {'status': 'error'}, 400

    if not email == 'admin@admin.com':
        return {'status': 'error'}, 400
    if not password == 'lera73':
        return {'status': 'error'}, 400

    identity = {'email': email}
    access_token = create_access_token(identity=identity, expires_delta=timedelta(hours=240))
    return {'status': 'success', 'token': access_token}, 200


@mod_auth.route('/user/get', methods=['GET'])
def return_user():
    return {'status': 'success', 'user': 'admin@admin.com'}, 200
