from BD.bd import engine
from sqlalchemy.orm import sessionmaker
from flask import Blueprint, request, jsonify
from models.treino import Treino

treino_route = Blueprint('route_treino', __name__)

@treino_route.route('/CadastrarTreino', methods=['POST'])
def CadastrarTreino():
    data = request.get_json()
    objetivo = data.get('objetivo')
    descricao = data.get('descricao')
    id_aluno = data.get('id_aluno')
    session = sessionmaker(bind=engine)()
    try:
        treino = Treino(objetivo, descricao, id_aluno)
        treino.CadastrarTreino(session)
        session.commit()
        return jsonify({"mensagem": "Treino cadastrado com sucesso!", "dados": data}), 201
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao cadastrar treino", "erro": str(e)}), 404
    finally:
        session.close()

