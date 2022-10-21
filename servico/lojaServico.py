from repositorio.lojaRepositorio import LojaRepositorio

class LojaServico:

    def inserirLoja(loja):
        LojaRepositorio().inserirLoja(loja)
        resposta = {
                    'codigo':0,
                    'mensagem':'Operação realizada com sucesso',
                    'loja':{
                            'id':loja['_id'],
                            'nome':loja['nome'],
                            'documentoFiscal':loja['documentoFiscal'],
                            'email':loja['email'],
                            'telefone':loja['telefone'],
                            'cep':loja['cep'],
                            'logradouro':loja['logradouro'],
                            'numero':loja['numero'],
                            'bairro':loja['bairro'],
                            'cidade':loja['cidade'],
                            'uf':loja['uf'],
                            'complemento':loja['complemento']
                            }
                    }
        return resposta

    def atualizarLoja(loja):
        loja = {
                '_id':loja['id'],
                'nome':loja['nome'],
                'documentoFiscal':loja['documentoFiscal'],
                'email':loja['email'],
                'telefone':loja['telefone'],
                'cep':loja['cep'],
                'logradouro':loja['logradouro'],
                'numero':loja['numero'],
                'bairro':loja['bairro'],
                'cidade':loja['cidade'],
                'uf':loja['uf'],
                'complemento':loja['complemento']
                }
        LojaRepositorio().atualizarLoja(loja['_id'], loja)
        resposta = {
                    'codigo':0,
                    'mensagem':'Operação realizada com sucesso',
                    'loja':{
                            'id':loja['_id'],
                            'nome':loja['nome'],
                            'documentoFiscal':loja['documentoFiscal'],
                            'email':loja['email'],
                            'telefone':loja['telefone'],
                            'cep':loja['cep'],
                            'logradouro':loja['logradouro'],
                            'numero':loja['numero'],
                            'bairro':loja['bairro'],
                            'cidade':loja['cidade'],
                            'uf':loja['uf'],
                            'complemento':loja['complemento']
                            }
                    }
        return resposta

    def buscarLoja(id):
        id = int(id)
        for loja in LojaRepositorio().buscarLoja(id):
            resposta = {
                        'codigo':0,
                        'mensagem':'Operação realizada com sucesso',
                        'loja':{
                                'id':loja['_id'],
                                'nome':loja['nome'],
                                'documentoFiscal':loja['documentoFiscal'],
                                'email':loja['email'],
                                'telefone':loja['telefone'],
                                'cep':loja['cep'],
                                'logradouro':loja['logradouro'],
                                'numero':loja['numero'],
                                'bairro':loja['bairro'],
                                'cidade':loja['cidade'],
                                'uf':loja['uf'],
                                'complemento':loja['complemento']
                                }
                        }
            return resposta
        
    def listarLojas():
        resposta = {}
        lojas = []
        for loja in LojaRepositorio().listarLojas():
            loja = {
                            'id':loja['_id'],
                            'nome':loja['nome'],
                            'documentoFiscal':loja['documentoFiscal'],
                            'email':loja['email'],
                            'telefone':loja['telefone'],
                            'cep':loja['cep'],
                            'logradouro':loja['logradouro'],
                            'numero':loja['numero'],
                            'bairro':loja['bairro'],
                            'cidade':loja['cidade'],
                            'uf':loja['uf'],
                            'complemento':loja['complemento']
                            }
            lojas.append(loja)
            resposta = {'codigo':0,
                        'mensagem':'Operação realizada com sucesso',
                        'lojas':lojas}
        return resposta

    def deletarLoja(id):
        LojaRepositorio().deletarLoja(id)
