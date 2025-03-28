from flask import Blueprint, request, jsonify
from models.aluno import Aluno
from models.endereco import Endereco
from models.plano import Plano
from BD.bd import engine
from sqlalchemy.orm import sessionmaker


aluno_route = Blueprint('aluno', __name__)


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
    lista_aulas_id = data.get('aulas_id') or []
    lista_treinos_id = data.get('treinos_id') or []

    sessionLocal = sessionmaker(bind=engine)
    session = sessionLocal()

    try:
        aluno = Aluno(matricula, nome, data_nascimento, cpf, email, telefone, plano_id)
        aluno.CadastrarAluno(session)
        end = Endereco(logradouro, cep, rua, num_casa, bairro, cidade, matricula, None)
        end.CadastrarEndereco(session)
        for aula_id in lista_aulas_id:
            aluno.CadastrarAlunoAula(aula_id, session)
        for treino_id in lista_treinos_id:
            aluno.CadastrarAlunoTreino(treino_id, session)

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
    session = sessionmaker(bind=engine)()
    
    try:
        aluno = Aluno(0, "", "", "", "", "", 0)
        result = aluno.ListarAluno(session)
        
        alunos = [
            {"matricula": row[0], "nome": row[1], "data_nascimento": row[2], "cpf": row[3], "email": row[4], "telefone": row[5]}
            for row in result
        ]
        return jsonify({"alunos": alunos}), 200
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao listar alunos"}), 404



@aluno_route.route('/FormAtualizarAluno/<int:matricula>', methods=['GET'])
def FormAtualizarAluno(matricula):
    session = sessionmaker(bind=engine)()
        
    try:
        aluno = Aluno(matricula, "", "", "", "", "", 0, 0)
        resultAluno = aluno.GetAllAluno(session)

        dictAluno = {
        "aluno": {
            "matricula": resultAluno[0],
            "nome": resultAluno[1],
            "data_nascimento": resultAluno[2],
            "cpf": resultAluno[3],
            "email": resultAluno[4],
            "telefone": resultAluno[5]
        },
        "endereco": {
            "logradouro": resultAluno[6],
            "cep": resultAluno[7],
            "rua": resultAluno[8],
            "num_casa": resultAluno[9],
            "bairro": resultAluno[10],
            "cidade": resultAluno[11]
        },
        "plano": {
            "nome_plano": resultAluno[12],
            "valor_plano": resultAluno[13],
            "descricao_plano": resultAluno[14]
        },
        "ids_treino": resultAluno[15],
        "ids_aula": resultAluno[16]
    }


        return jsonify({"aluno": dictAluno}), 200
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"mensagem": f"Error ao selecionar aluno - {e}"}), 404





@aluno_route.route('/AtualizarAluno', methods=['PATCH'])
def AtualizarAluno():
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
    lista_aulas_id = data.get('aulas_id')

    sessionLocal = sessionmaker(bind=engine)
    session = sessionLocal()

    try:
        aluno = Aluno(matricula, nome, data_nascimento, cpf, email, telefone, id_end, plano_id)
        ids = aluno.AtualizarAluno(session)
        print(ids)
        end = Endereco(logradouro, cep, rua, num_casa, bairro, cidade)
        id_end = end.CadastrarEndereco(ids[0], session)
        
        for aula_id in lista_aulas_id:
            aluno.CadastrarAlunoAula(aula_id, session)
        session.commit()
        return jsonify({"mensagem": "Aluno cadastrado com sucesso!", "dados": data}), 201
    
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao cadastrar aluno", "erro": str(e)}), 404
    
    finally:
        session.close()


@aluno_route.route('/ExcluirAluno/<int:matricula>', methods=['DELETE'])
def ExcluirAluno(matricula):
    session = sessionmaker(bind=engine)()
    try:
        aluno = Aluno(matricula, "", "", "", "", "", 0)
        aluno.ExcluirAluno(matricula, session)
        session.commit()
        return jsonify({"mensagem": "Aluno excluído com sucesso!"}), 200
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao excluir aluno", "erro": str(e)}), 404
    finally:
        session.close()