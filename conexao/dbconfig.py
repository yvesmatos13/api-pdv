from pymongo import MongoClient


class Conexao():

    def __init__(self, colecao):
        self.colecao = colecao

    def pdvDS(self):
        cliente = MongoClient('mongodb://172.17.0.3:27017/')
        database = cliente['pdv']
        return database[self.colecao]
