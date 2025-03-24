from flask import Blueprint, request, jsonify
from models.aparelho import Aparelho


gestMaterial_route = Blueprint('gestMaterial', __name__)


@gestMaterial_route.route('/FormCadastrarAparelho', methods=['GET'])
def FormCadastrarVisitante():
    ...

@gestMaterial_route.route('/CadastrarAparelho', methods=['POST'])
def CadastrarAparelho():
    data = request.get_json()  # Obtém o JSON enviado
    nome = data.get('nome')
    quantidade = data.get('quantidade')
    disponibilidade = data.get('disponibilidade')
    
    aparelho  = Aparelho(nome, quantidade, disponibilidade)
    result = aparelho.CadastrarAparelho()

    if result:
        return jsonify({"mensagem": "Aparelho cadastrado com sucesso!", "dados": data}), 201
    
    return jsonify({"mensagem": "error"}), 404


@gestMaterial_route.route('/ListarAparelhos', methods=['GET'])
def ListarAparelhos():
    aparelho = Aparelho("", "", "")
    result = aparelho.ListarAparelhos()
    if result:
        aparelhos = [
            {"id_aparelho": row[0], "nome": row[1], "quantidade": row[2], "disponibilidade": row[3]}
            for row in result
        ]
        return jsonify({"Aparelhos": aparelhos}), 200
    
    elif result == []:
        return jsonify({"mensagem": "Nenhum aparelho encontrado"}), 404
    
    return jsonify({"mensagem": "Erro ao listar aparelhos"}), 404



@gestMaterial_route.route('/FormAtualizarAparelho/<int:id_aparelho>', methods=['GET'])
def FormAtualizarVisitante(id_aparelho):
    aparelho = Aparelho("", "", "")
    resultAparelho = aparelho.GetAparelho(id_aparelho)
    if resultAparelho:
        result = resultAparelho[0]
        aparelho = {"id_aparelho": result[0], "nome": result[1], "quantidade": result[2], "disponibilidade": result[3]}
        return jsonify({"aparelho": aparelho}), 200
        
    return jsonify({"mensagem": "Error ao selecionar aparelho"}), 404


@gestMaterial_route.route('/AtualizarAparelho', methods=['PUT'])
def AtualizarVisitante():
    data = request.get_json()  # Obtém o JSON enviado
    id_aparelho = data.get('id_aparelho')
    nome = data.get('nome')
    quantidade = data.get('quantidade')
    disponibilidade = data.get('disponibilidade')
    
    aparelho  = Aparelho(nome, quantidade, disponibilidade)
    result = aparelho.AtualizarAparelho(id_aparelho)
    if result:
        return jsonify({"mensagem": "Aparelho atualizado com sucesso!"}), 200
    if result is None:
        return jsonify({"mensagem": "Aparelho não encontrado"}), 404
    return jsonify({"mensagem": "Erro ao atualizar aparelho"}), 404

@gestMaterial_route.route('/RemoverAparelho/<int:id_aparelho>', methods=['DELETE'])
def RemoverVisitante(id_aparelho):
    aparelho = Aparelho("", "", "")
    result = aparelho.RemoverAparelho(id_aparelho)

    if result:
        return jsonify({"mensagem": "Aparelho removido com sucesso!"}), 200
    elif result is None:
        return jsonify({"mensagem": "Aparelho não encontrado"}), 404
    return jsonify({"mensagem": "Erro ao remover aparelho"}), 404