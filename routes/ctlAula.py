from flask import Blueprint, request, jsonify
from models.aula import Aula
from sqlalchemy.orm import sessionmaker
from BD.bd import engine

aula_route = Blueprint('aula', __name__)

@aula_route.route('/CadastrarAula', methods=['POST'])
def CadastrarAula():
    data = request.get_json()
    horario = data.get('horario')
    tipo = data.get('tipo')
    sala = data.get('sala')
    session = sessionmaker(bind=engine)()
    try:
        aula = Aula(horario, tipo, sala)
        aula.CadastrarAula(session)
        session.commit()
        return jsonify({"mensagem": "Aula cadastrada com sucesso!", "dados": data}), 201
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao cadastrar aula", "erro": str(e)}), 404
    finally:
        session.close()


@aula_route.route('/ListarAula', methods=['GET'])
def ListarAula():
    session = sessionmaker(bind=engine)()
    try:
        aula = Aula("", "", "")
        result = aula.ListarAula(session)
        aulas = [
            {"id_aula": row[0], "horario": row[1], "tipo": row[2], "sala": row[3]}
            for row in result
        ]
        return jsonify({"aulas": aulas}), 200
    except Exception as e:  
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao listar aulas", "erro": str(e)}), 404
    finally:
        session.close()
        