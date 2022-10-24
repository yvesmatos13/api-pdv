from repositorio.lojaRepositorio import LojaRepositorio

class LojaServico:

    def inserirLoja(loja):
        loja = loja = {
            'nome': loja['nome'],
            'documentoFiscal': loja['documentoFiscal'],
            'email': loja['email'],
            'telefone': loja['telefone'],
            'cep': loja['cep'],
            'logradouro': loja['logradouro'],
            'numero': loja['numero'],
            'bairro': loja['bairro'],
            'cidade': loja['cidade'],
            'uf': loja['uf'],
            'complemento': loja['complemento']
        }
        LojaRepositorio().inserirLoja(loja)
        resposta = {
            'id': loja['_id'],
            'nome': loja['nome'],
            'documentoFiscal': loja['documentoFiscal'],
            'email': loja['email'],
            'telefone': loja['telefone'],
            'cep': loja['cep'],
            'logradouro': loja['logradouro'],
            'numero': loja['numero'],
            'bairro': loja['bairro'],
            'cidade': loja['cidade'],
            'uf': loja['uf'],
            'complemento': loja['complemento']
        }

        return resposta

    def atualizarLoja(loja):
        loja = {
            '_id': loja['id'],
            'nome': loja['nome'],
            'documentoFiscal': loja['documentoFiscal'],
            'email': loja['email'],
            'telefone': loja['telefone'],
            'cep': loja['cep'],
            'logradouro': loja['logradouro'],
            'numero': loja['numero'],
            'bairro': loja['bairro'],
            'cidade': loja['cidade'],
            'uf': loja['uf'],
            'complemento': loja['complemento']
        }
        LojaRepositorio().atualizarLoja(loja['_id'], loja)
        resposta = {
            'id': loja['_id'],
            'nome': loja['nome'],
            'documentoFiscal': loja['documentoFiscal'],
            'email': loja['email'],
            'telefone': loja['telefone'],
            'cep': loja['cep'],
            'logradouro': loja['logradouro'],
            'numero': loja['numero'],
            'bairro': loja['bairro'],
            'cidade': loja['cidade'],
            'uf': loja['uf'],
            'complemento': loja['complemento']
        }

        return resposta

    def buscarLoja(id):
        id = int(id)
        for loja in LojaRepositorio().buscarLoja(id):
            resposta = {
                'id': loja['_id'],
                'nome': loja['nome'],
                'documentoFiscal': loja['documentoFiscal'],
                'email': loja['email'],
                'telefone': loja['telefone'],
                'cep': loja['cep'],
                'logradouro': loja['logradouro'],
                'numero': loja['numero'],
                'bairro': loja['bairro'],
                'cidade': loja['cidade'],
                'uf': loja['uf'],
                'complemento': loja['complemento']
            }
            return resposta

    def listarLojas():
        resposta = {}
        lojas = []
        for loja in LojaRepositorio().listarLojas():
            loja = {
                'id': loja['_id'],
                'nome': loja['nome'],
                'documentoFiscal': loja['documentoFiscal'],
                'email': loja['email'],
                'telefone': loja['telefone'],
                'cep': loja['cep'],
                'logradouro': loja['logradouro'],
                'numero': loja['numero'],
                'bairro': loja['bairro'],
                'cidade': loja['cidade'],
                'uf': loja['uf'],
                'complemento': loja['complemento']
            }
            lojas.append(loja)
            resposta = {
                        'lojas': lojas
                        }
        return resposta

    def deletarLoja(id):
        LojaRepositorio().deletarLoja(id)
