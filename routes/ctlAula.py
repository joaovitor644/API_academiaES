from flask import Blueprint, request, jsonify
from models.aula import Aula

aula_route = Blueprint('aula', __name__)

@aula_route.route('/CadastrarAula', methods=['POST'])
def CadastrarAula():
    data = request.get_json()
    horario = data.get('horario')
    tipo = data.get('tipo')
    sala = data.get('sala')
    id_funcionario = data.get('id_funcionario')
    id_aluno = data.get('id_aluno')
    aula = Aula(horario, tipo, sala, id_funcionario, id_aluno)
    result = aula.CadastrarAula()
    if result:
        return jsonify({"mensagem": "Aula cadastrada com sucesso!", "dados": data}), 201
    return jsonify({"mensagem": "Erro ao cadastrar aula"}), 404


@aula_route.route('/ListarAula', methods=['GET'])
def ListarAula():
    aula = Aula("", "", "", 0, 0)
    result = aula.ListarAula()
    if result:
        aulas = [
            {"id_aula": row[0], "horario": row[1], "tipo": row[2], "sala": row[3]}
            for row in result
        ]
        return jsonify({"aulas": aulas}), 200
    return jsonify({"mensagem": "Erro ao listar aulas"}), 404