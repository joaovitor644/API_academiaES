from flask import Blueprint, request, jsonify, session
from werkzeug.security import check_password_hash , generate_password_hash
import hashlib
from sqlalchemy.orm import sessionmaker
from BD.bd import engine
from models.login import Login

auth = Blueprint('auth', __name__)

# Configuração da sessão (adicionar no seu app.py ou onde você inicializa o Flask)
# app.secret_key = 'sua_chave_secreta_aqui'

@auth.route('/auth', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Usuário e senha são obrigatórios'}), 400

    # Busca o usuário no banco de dados
    login1 = Login(username, password)
    user_info = login1.Auth()
    print(user_info)
    if not user_info:
        return jsonify({'message': 'Usuário não encontrado'}), 404

    # Verifica a senha
    stored_password_hash = user_info[3]  # Supondo que o hash da senha esteja na posição 3
    if hashlib.sha256(password.encode()).hexdigest() == stored_password_hash:
        session['user'] = username
        session['is_admin'] = user_info[4]  # Supondo que o campo is_admin esteja na posição 4
        return jsonify({'message': 'Login bem-sucedido'}), 200

# Suponha que user_info e password sejam definidos anteriormente no código
    return jsonify({
        'message': 'Credenciais inválidas'
    }), 401


@auth.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    session.pop('is_admin', None)
    return jsonify({'message': 'Logoff bem-sucedido'}), 200

@auth.route('/session', methods=['GET'])
def get_session():
    user = session.get('user')
    is_admin = session.get('is_admin')
    login1 = Login(user, '_')
    user_info = login1.Auth()
    if user_info:
        return jsonify({'permission': 'OK', 'user': user, 'isAdm': is_admin}), 200
    return jsonify({'permission': 'ERR'}), 401