from flask import request, jsonify, Blueprint
from BD.bd import engine
from sqlalchemy.orm import sessionmaker
from models.funcionario import Funcionario
from models.endereco import Endereco
from models.adm import Adm
from models.instrutor import Instrutor
from models.contrato import Contrato

funcionario_route = Blueprint('funcionario', __name__)

@funcionario_route.route('/CadastrarFuncionario', methods=['POST'])
def CadastrarFuncionario():
    data = request.get_json()
    nit = data.get('nit')
    nome = data.get('nome')
    data_nascimento = data.get('data_nascimento')
    cpf = data.get('cpf')
    email = data.get('email')
    telefone = data.get('telefone')
    logradouro = data.get('logradouro')
    cep = data.get('cep')
    rua = data.get('rua')
    num_casa = data.get('num_casa')
    bairro = data.get('bairro')
    cidade = data.get('cidade')
    is_admin = data.get('is_admin')
    cargo = data.get('cargo')
    grau_academico = data.get('grau_academico')
    salario = data.get("salario")
    data_contratacao = data.get("data_contratacao")
    data_final = data.get("data_final")

    session = sessionmaker(bind=engine)()

    try:
        contrato = Contrato(salario, data_contratacao, data_final)
        id_contrato = contrato.CadastrarContrato(session)

        end = Endereco(logradouro, cep, rua, num_casa, bairro, cidade)
        id_endereco = end.CadastrarEndereco(session)

        funcionario = Funcionario(nit, nome, data_nascimento, cpf, email, telefone, id_endereco, id_contrato)
        funcionario.CadastrarFuncionario(session)
        
        if is_admin:
            adm = Adm(nit, cargo)
            adm.CadastrarAdm(session)
        else:
            instrutor = Instrutor(nit, grau_academico)
            instrutor.CadastrarInstrutor(session)
        
        session.commit()
        return jsonify({"mensagem": "Funcionário cadastrado com sucesso!", "dados": data}), 201
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao cadastrar funcionário", "erro": str(e)}), 404
    finally:
        session.close()


@funcionario_route.route('/ListarFuncionarios', methods=['GET'])
def ListarFuncionarios():
    session = sessionmaker(bind=engine)()
    try:
        funcionario = Funcionario("", "", "", "", "", "", "", "")
        result = funcionario.ListarFuncionarios(session)
        funcionarios = [
            {"nit": row[0], "nome": row[1], "data_nascimento": row[2], "cpf": row[3], "email": row[4], "telefone": row[5], "id_endereco": row[6], "id_contrato": row[7]}
            for row in result
        ]
        return jsonify({"funcionarios": funcionarios}), 200
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao listar funcionários", "erro": str(e)}), 404
    finally:
        session.close()


@funcionario_route.route('/FormAtualizarFuncionario/<string:nit>', methods=['GET'])
def FormAtualizarFuncionario(nit):
    session = sessionmaker(bind=engine)()
    try:
        funcionario = Funcionario(nit, "", "", "", "", "", "")
        result = funcionario.GetAllFuncionario(session)
        chaves = [
            "NIT", "nome", "data_nascimento", "cpf", "email", "telefone", "endereco_id_endereco",
            "id_usuario", "username", "is_admin",
            "cargo_administrador",
            "grau_instrutor",
            "id_contrato", "salario", "data_contratacao", "data_final",
            "logradouro", "cep", "rua", "num_casa", "bairro", "cidade"
        ]

        dict_funcionario = dict(zip(chaves, result))

        return jsonify({"funcionario": dict_funcionario}), 200
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao buscar funcionário", "erro": str(e)}), 404
    finally:
        session.close()