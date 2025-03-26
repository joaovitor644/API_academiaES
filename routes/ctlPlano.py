from flask import Blueprint, request
from sqlalchemy.orm import sessionmaker
from BD.bd import engine

from models.plano import Plano

plano_route = Blueprint('plano', __name__)

@plano_route.route('/FormCadastrarPlano', methods=['GET'])
def FormCadastrarPlano():
    return {"mensagem": "Formulário de cadastro de plano"}


@plano_route.route('/CadastrarPlano', methods=['POST'])
def CadastrarPlano():
    data = request.get_json()
    nome = data.get('nome')
    valor = data.get('valor')
    descricao = data.get('descricao')
    sessionLocal = sessionmaker(bind=engine)
    session = sessionLocal()
    try:
        plano = Plano(nome, valor, descricao)
        plano.CadastrarPlano(session)
        session.commit()
        return {"mensagem": "Plano cadastrado com sucesso!"}, 201
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return {"mensagem": "Erro ao cadastrar plano", "erro": str(e)}, 404
    finally:
        session.close()
    
@plano_route.route('/ListarPlano', methods=['GET'])
def ListarPlano():
    sessionLocal = sessionmaker(bind=engine)
    session = sessionLocal()

    try:
        plano = Plano("", 0.0, "")
        result = plano.ListarPlano(session)
        planos = [
            {"id": row[0], "nome": row[1], "valor": row[2], "descricao": row[3]}
            for row in result
        ]
        session.commit()
        return {"planos": planos}, 200
    except Exception as e:
        print(f"Erro: {e}")
        return {"mensagem": "Erro ao listar planos", "erro": str(e)}, 404
    finally:
        session.close()