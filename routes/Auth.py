from flask import Blueprint, request, jsonify,session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from BD.bd import engine
from sqlalchemy.sql import text

auth = Blueprint('auth', __name__)

users = {
    "casa": generate_password_hash("123", method='pbkdf2:sha256'),
}

@auth.route('/auth', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    hashed_password = users.get(username)

    if hashed_password and check_password_hash(hashed_password, password):
        session['user'] = username
        return jsonify({'message': 'Login bem-sucedido'}), 200
    
    return jsonify({'message': 'Credenciais inválidas'}), 401

@auth.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({'message': 'Logoff bem-sucedido'}), 200

@auth.route('/session', methods=['GET'])
def get_session():
    user = session.get('user')
    if user:
        return jsonify({'permission':'OK', 'user':user, 'isAdm':True}), 200
    return jsonify({'permission': 'ERR'}), 401 