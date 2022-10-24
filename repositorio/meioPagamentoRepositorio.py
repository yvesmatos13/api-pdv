from conexao.dbconfig import Conexao
from repositorio.sequenceId import SequenceId

class MeioPagamentoRepositorio():

    def __init__(self):
        self.colecao = 'meiopagamento'

    def inserirMeioPagamento(self, meiopagamento):
        meiopagamento['_id'] = SequenceId(self.colecao).nextId()
        Conexao(self.colecao).pdvDS().insert_one(meiopagamento)

    def atualizarMeioPagamento(self, id, meiopagamento):
        Conexao(self.colecao).pdvDS().update_one({'_id': id}, {'$set':meiopagamento})

    def buscarMeioPagamento(self, id):
        return Conexao(self.colecao).pdvDS().find({'_id': id})

    def listarMeioPagamentos(self):
        return Conexao(self.colecao).pdvDS().find()

    def deletarMeioPagamento(self, id):
        Conexao(self.colecao).pdvDS().delete_one({'_id': id})
