from flask import Blueprint, request, jsonify
from models.aluno import Aluno
from models.endereco import Endereco
from BD.bd import engine
from sqlalchemy.orm import sessionmaker


aluno_route = Blueprint('aluno', __name__)


@aluno_route.route('/FormCadastrarAluno', methods=['GET'])
def FormCadastrarAluno():
    ...

@aluno_route.route('/CadastrarAluno', methods=['POST'])
def CadastrarAluno():
    data = request.get_json()  
    matricula = data.get('matricula')
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
    plano_id = data.get('plano_id')

    sessionLocal = sessionmaker(bind=engine)
    session = sessionLocal()

    try:
        end = Endereco(logradouro, cep, rua, num_casa, bairro, cidade)
        id_end = end.CadastrarEndereco(session)
        aluno = Aluno(matricula, nome, data_nascimento, cpf, email, telefone, id_end, plano_id)
        aluno.CadastrarAluno(session)
        session.commit()
        return jsonify({"mensagem": "Aluno cadastrado com sucesso!", "dados": data}), 201
    
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao cadastrar aluno", "erro": str(e)}), 404
    
    finally:
        session.close()



@aluno_route.route('/ListarAluno', methods=['GET'])
def ListarAluno():
    aluno = Aluno(0, "", "", "", "", "", 0, 0)
    result = aluno.ListarAluno()
    if result:
        alunos = [
            {"matricula": row[0], "nome": row[1], "data_nascimento": row[2], "cpf": row[3], "email": row[4], "telefone": row[5], "endereco_id": row[6], "plano_id": row[7]}
            for row in result
        ]
        return jsonify({"alunos": alunos}), 200
    return jsonify({"mensagem": "Erro ao listar alunos"}), 404



@aluno_route.route('/FormAtualizarAluno/<int:matricula>', methods=['GET'])
def FormAtualizarAluno(matricula):
    try:
        sessionLocal = sessionmaker(bind=engine)
        session = sessionLocal()

        aluno = Aluno(matricula, "", "", "", "", "", 0, 0)
        resultAluno = aluno.GetAluno(session)
        result = resultAluno[6]

        endereco = Endereco(0, "", "", 0, "", "")
        print(type(result))
        result_endereco = endereco.GetEndereco(result, session)

        aluno = {"matricula": resultAluno[0], "nome": resultAluno[1], "data_nascimento": resultAluno[2], "cpf": resultAluno[3],
        "email": resultAluno[4], "telefone": resultAluno[5], "endereco_id": resultAluno[6],
        "plano_id": resultAluno[7], "logradouro": result_endereco[1], "cep": result_endereco[2],
        "rua": result_endereco[3], "num_casa": result_endereco[4], "bairro": result_endereco[5], "cidade": result_endereco[6]}
        return jsonify({"aluno": aluno}), 200
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"mensagem": f"Error ao selecionar aluno - {e}"}), 404



@aluno_route.route('/FormAtualizarAlunoAula', methods=['GET'])
def FormAtualizarAlunoAula():
    ...


@aluno_route.route('/AtualizarAluno', methods=['PATCH'])
def AtualizarAluno():
    data = request.get_json()
    matricula = data.get('matricula')
    nome = data.get('nome')
    data_nascimento = data.get('data_nascimento')
    cpf = data.get('cpf')
    email = data.get('email')
    telefone = data.get('telefone')
    plano_id = data.get('plano_id')
    aluno = Aluno(matricula, nome, data_nascimento, cpf, email, telefone, 0, plano_id)
    result = aluno.AtualizarAluno()
    if result:
        return jsonify({"mensagem": "Aluno atualizado com sucesso!"}), 200
    return jsonify({"mensagem": "Erro ao atualizar aluno"}), 404