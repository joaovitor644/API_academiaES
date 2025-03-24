from flask import Blueprint, request

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
    plano = Plano(nome, valor, descricao)
    result = plano.CadastrarPlano()
    if result:
        return {"mensagem": "Plano cadastrado com sucesso!"}, 201
    return {"mensagem": "Erro ao cadastrar plano"}, 404
    
@plano_route.route('/ListarPlano', methods=['GET'])
def ListarPlano():
    plano = Plano("", 0.0, "")
    result = plano.ListarPlano()
    if result:
        planos = [
            {"id": row[0], "nome": row[1], "valor": row[2], "descricao": row[3]}
            for row in result
        ]
        return {"planos": planos}, 200
    return {"mensagem": "Erro ao listar planos"}, 404