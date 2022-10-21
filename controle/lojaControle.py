import json
from pickle import FALSE
from flask import Blueprint, jsonify, request
from flask_api import status
from servico.lojaServico import LojaServico

loja_blueprint = Blueprint("Loja", __name__)

class LojaControle:

    @loja_blueprint.route('/novaLoja', methods=['POST'])
    def inserirLoja():
        loja = json.loads(request.data)
        return jsonify(LojaServico.inserirLoja(loja)), status.HTTP_201_CREATED

    @loja_blueprint.route('/editarLoja', methods=['PUT'])
    def atualizarLoja():
        loja = json.loads(request.data)
        return jsonify(LojaServico.atualizarLoja(loja)), status.HTTP_200_OK

    @loja_blueprint.route('/loja', methods=['GET'])
    def buscarLoja():
        args = request.args
        id = args.get('id')
        return jsonify(LojaServico.buscarLoja(id)), status.HTTP_200_OK

    @loja_blueprint.route('/lojas', methods=['GET'])
    def listarLojas():
        return jsonify(LojaServico.listarLojas()), status.HTTP_200_OK