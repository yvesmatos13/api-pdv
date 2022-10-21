from conexao.dbconfig import Conexao
from repositorio.sequenceId import SequenceId

class LojaRepositorio():

    def __init__(self):
        self.colecao = 'loja'

    def inserirLoja(self, loja):
        loja['_id'] = SequenceId(self.colecao).nextId()
        Conexao(self.colecao).pdvDS().insert_one(loja)

    def atualizarLoja(self, id, loja):
        Conexao(self.colecao).pdvDS().update_one({'_id': id}, {'$set':loja})

    def buscarLoja(self, id):
        return Conexao(self.colecao).pdvDS().find({'_id': id})

    def listarLojas(self):
        return Conexao(self.colecao).pdvDS().find()

    def deletarLoja(self, id):
        Conexao(self.colecao).pdvDS().delete_one({'_id': id})
