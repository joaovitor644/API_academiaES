from flask import Blueprint, request
from models.instrutor import Instrutor
from models.endereco import Endereco
from models.login import Login
from BD.bd import engine
from sqlalchemy.orm import sessionmaker

instrutor_route = Blueprint('instrutor', __name__)

@instrutor_route.route('/FormCadastrarInstrutor', methods=['GET'])
def FormCadastrarInstrutor():
    return {"mensagem": "Formulário de cadastro de instrutor"}

@instrutor_route.route('/CadastrarInstrutor', methods=['POST'])
def CadastrarInstrutor():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    is_adm = data.get('is_adm')
    logradouro = data.get('logradouro')
    cep = data.get('cep')
    rua = data.get('rua')
    num_casa = data.get('num_casa')
    bairro = data.get('bairro')
    cidade = data.get('cidade')
    nit = data.get('nit')
    nome = data.get('nome')
    data_nascimento = data.get('data_nascimento')
    cpf = data.get('cpf')
    email = data.get('email')
    telefone = data.get('telefone')
    grau_academico = data.get('grau_academico')
        
    sessionLocal = sessionmaker(bind=engine)
    session = sessionLocal()
    
    try:
        user = Login(username, password, is_adm)
        id_usuario = user.CadastrarUser(session)

        endereco = Endereco(logradouro, cep, rua, num_casa, bairro, cidade)
        id_endereco = endereco.CadastrarEndereco(session)

        instrutor = Instrutor(nit, nome, data_nascimento, cpf, email, telefone, id_endereco, id_usuario, grau_academico)
        instrutor.CadastrarInstrutor(session)
        session.commit()
        return {"mensagem": "Adm cadastrado com sucesso!"}, 201
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return {"mensagem": f"Erro ao cadastrar adm - {e}"}, 404
    finally:
        session.close()