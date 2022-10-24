import json
from pickle import FALSE
from flask import Blueprint, jsonify, request
from flask_api import status
from servico.meioPagamentoServico import MeioPagamentoServico


meioPagamento_blueprint = Blueprint("meioPagamento", __name__)

class MeioPagamentoControle:

    @meioPagamento_blueprint.route('/novoMeioPagamento', methods=['POST'])
    def inserirMeioPagamento():
        meioPagamento = json.loads(request.data)
        return jsonify(MeioPagamentoServico.inserirMeioPagamento(meioPagamento)), status.HTTP_201_CREATED

    @meioPagamento_blueprint.route('/editarMeioPagamento', methods=['PUT'])
    def atualizarMeioPagamento():
        meioPagamento = json.loads(request.data)
        return jsonify(MeioPagamentoServico.atualizarMeioPagamento(meioPagamento)), status.HTTP_200_OK

    @meioPagamento_blueprint.route('/buscarMeioPagamento', methods=['GET'])
    def buscarMeioPagamento():
        args = request.args
        id = args.get('id')
        return jsonify(MeioPagamentoServico.buscarMeioPagamento(id)), status.HTTP_200_OK

    @meioPagamento_blueprint.route('/listarMeioPagamentos', methods=['GET'])
    def listarMeioPagamentos():
        return jsonify(MeioPagamentoServico.listarMeioPagamentos()), status.HTTP_200_OK