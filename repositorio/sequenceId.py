from conexao.dbconfig import Conexao


class SequenceId():

    def __init__(self, colecao):
        self.colecao = colecao

    def nextId(self):
        lastId = list(Conexao(self.colecao).pdvDS(
        ).find().sort('_id', -1).limit(1))
        nextId = None
        if lastId:
            for lastId in Conexao(self.colecao).pdvDS().find().sort('_id', -1).limit(1):
                nextId = lastId['_id'] + 1

        elif not lastId:
            nextId = 1
        return nextId
