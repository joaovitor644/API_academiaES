from flask import Blueprint, request, jsonify
from models.visitante import Visitante
from models.endereco import Endereco


visitante_route = Blueprint('visitante', __name__)


@visitante_route.route('/FormCadastrarVisitante', methods=['GET'])
def FormCadastrarVisitante():
    ...

@visitante_route.route('/CadastrarVisitante', methods=['POST'])
def CadastrarVisitante():
    data = request.get_json()  # Obtém o JSON enviado
    nome = data.get('nome')
    data_visita = data.get('data_visita')
    telefone = data.get('telefone')
    qunt_visitas = data.get('qunt_visitas')
    
    logradouro = data.get('logradouro')
    cep = data.get('cep')
    rua = data.get('rua')
    num_casa = data.get('num_casa')
    bairro = data.get('bairro')
    cidade = data.get('cidade')

    endereco = Endereco(logradouro, cep, rua, num_casa, bairro, cidade)
    id_end = endereco.CadastrarEndereco()
    
    visitante  = Visitante(nome, data_visita, telefone, qunt_visitas, id_end)
    result = visitante.CadastrarVisitante()

    if result:
        return jsonify({"mensagem": "Visitante cadastrado com sucesso!", "dados": data}), 201
    
    return jsonify({"mensagem": "error!", "dados": id_end}), 404


@visitante_route.route('/ListarVisitantes', methods=['GET'])
def ListarVisitantes():
    visitante = Visitante("", "", "", "", "")
    result = visitante.ListarVisitantes()
    if result:
        visitantes = [
            {"id_visitantes": row[0], "nome": row[1], "data_visita": row[2], "telefone": row[3], "qunt_visitas": row[4], "endereco_id": row[5]}
            for row in result
        ]
        return jsonify({"visitantes": visitantes}), 200
    
    elif result == []:
        return jsonify({"mensagem": "Nenhum visitante encontrado"}), 404
    
    return jsonify({"mensagem": "Erro ao listar visitantes"}), 404



@visitante_route.route('/FormAtualizarVisitante/<int:id_visitante>', methods=['GET'])
def FormAtualizarVisitante(id_visitante):
    visitante = Visitante("", "", "", "", 0)
    resultVisitante = visitante.GetVisitante( id_visitante)
    if resultVisitante:
        result = resultVisitante[0]
        endereco = Endereco(0, "", "", 0, "", "")
        result_endereco = endereco.GetEndereco(result[5])
        if result_endereco:
            result_endereco = result_endereco[0]
            visitante = {"id_visitantes": result[0], "nome": result[1], "data_visita": result[2], "telefone": result[3],
            "qunt_visitas": result[4], "endereco_id": result[5], "logradouro": result_endereco[1], "cep": result_endereco[2],
            "rua": result_endereco[3], "num_casa": result_endereco[4], "bairro": result_endereco[5], "cidade": result_endereco[6]}
            return jsonify({"visitante": visitante}), 200
        
        return jsonify({"mensagem": "Error ao selecionar endereco"}), 404

    return jsonify({"mensagem": "Error ao selecionar visitante"}), 404


@visitante_route.route('/AtualizarVisitante', methods=['PUT'])
def AtualizarVisitante():
    data = request.get_json()  # Obtém o JSON enviado
    id_visitante = data.get('id_visitante')
    nome = data.get('nome')
    data_visita = data.get('data_visita')
    telefone = data.get('telefone')
    qunt_visitas = data.get('qunt_visitas')
    visitante = Visitante(nome, data_visita, telefone, qunt_visitas, 0)
    result = visitante.AtualizarVisitante(id_visitante)
    if result:
        return jsonify({"mensagem": "Visitante atualizado com sucesso!"}), 200
    if result is None:
        return jsonify({"mensagem": "Visitante não encontrado"}), 404
    return jsonify({"mensagem": "Erro ao atualizar visitante"}), 404

@visitante_route.route('/RemoverVisitante/<int:id_visitante>', methods=['DELETE'])
def RemoverVisitante(id_visitante):
    visitante = Visitante("", "", "", "", 0)
    result = visitante.RemoverVisitante(id_visitante)

    if result:
        return jsonify({"mensagem": "Visitante removido com sucesso!"}), 200
    elif result is None:
        return jsonify({"mensagem": "Visitante não encontrado"}), 404
    return jsonify({"mensagem": "Erro ao remover visitante"}), 404