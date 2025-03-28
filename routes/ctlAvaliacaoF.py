from flask import Blueprint, request, jsonify
from models.avaliacaoF import AvaliacaoF
from sqlalchemy.orm import sessionmaker
from BD.bd import engine



avaliacaoF_route = Blueprint('avaliacaoF', __name__)


@avaliacaoF_route.route('/CadastrarAvaliacaoF', methods=['POST'])
def CadastrarAvaliacaoF():
    data = request.get_json()
    peso = data.get('peso')
    altura = data.get('altura')
    data_avaliacao = data.get('data_avaliacao')
    id_aluno = data.get('id_aluno')
    session = sessionmaker(bind=engine)()
    try:
        avaliacaoF = AvaliacaoF(peso, altura, data_avaliacao, id_aluno)
        avaliacaoF.CadastrarAvaliacaoF(session)
        session.commit()
        return jsonify({"mensagem": "Avaliação física cadastrada com sucesso!", "dados": data}), 201
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao cadastrar avaliação física", "erro": str(e)}), 404
    finally:
        session.close()

        

@avaliacaoF_route.route('/ListarAvaliacaoF', methods=['GET'])
def ListarAvaliacaoF():
    session = sessionmaker(bind=engine)()
    try:
        avaliacaoF = AvaliacaoF(0.0, 0.0, "", 0)
        result = avaliacaoF.ListarAvaliacaoF(session)
        avaliacoesF = [
            {"id_avaliacaoF": row[0], "peso": row[1], "altura": row[2], "data_avaliacao": row[3], "id_aluno": row[4]}
            for row in result
        ]
        return jsonify({"avaliacoesF": avaliacoesF}), 200
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"mensagem": "Erro ao listar avaliações físicas", "erro": str(e)}), 404
    finally:
        session.close()