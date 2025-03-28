from BD.bd import engine
from sqlalchemy.orm import sessionmaker
from flask import Blueprint, request, jsonify
from models.treino import Treino

treino_route = Blueprint('route_treino', __name__)

@treino_route.route('/CadastrarTreino', methods=['POST'])
def CadastrarTreino():
    data = request.get_json()
    objetivo = data.get('objetivo')
    dificuldade = data.get('dificuldade')
    
    session = sessionmaker(bind=engine)()
    try:
        treino = Treino(objetivo, dificuldade)
        treino.CadastrarTreino(session)
        session.commit()
        return jsonify({"mensagem": "Treino cadastrado com sucesso!", "dados": data}), 201
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao cadastrar treino", "erro": str(e)}), 404
    finally:
        session.close()

@treino_route.route('/ListarTreinos', methods=['GET'])
def ListarTreinos():
    session = sessionmaker(bind=engine)()
    try:
        treino = Treino("", "")
        treinos = treino.ListarTrinos(session)
        dictTreinos = [{"id": row[0], "objetivo": row[1], "dificuldade": row[2]} for row in treinos]
        return jsonify({"mensagem": "Lista de treinos encontrada com sucesso!", "dados": dictTreinos}), 200
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao listar treinos", "erro": str(e)}), 404
    finally:
        session.close()