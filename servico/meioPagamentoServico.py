from repositorio.meioPagamentoRepositorio import MeioPagamentoRepositorio

class MeioPagamentoServico:

    def inserirMeioPagamento(meioPagamento):
        meioPagamento = meioPagamento = {
            'meioPagamento': meioPagamento['meioPagamento'],
            'pagamento': meioPagamento['pagamento'],
            'taxaOperadora': meioPagamento['taxaOperadora']
        }
        MeioPagamentoRepositorio().inserirMeioPagamento(meioPagamento)
        resposta = {
            'id': meioPagamento['_id'],
            'meioPagamento': meioPagamento['meioPagamento'],
            'pagamento': meioPagamento['pagamento'],
            'taxaOperadora': meioPagamento['taxaOperadora']
        }

        return resposta

    def atualizarMeioPagamento(meioPagamento):
        meioPagamento = {
            '_id': meioPagamento['id'],
            'meioPagamento': meioPagamento['meioPagamento'],
            'pagamento': meioPagamento['pagamento'],
            'taxaOperadora': meioPagamento['taxaOperadora']
        }
        MeioPagamentoRepositorio().atualizarMeioPagamento(meioPagamento['_id'], meioPagamento)
        resposta = {
            'id': meioPagamento['_id'],
            'meioPagamento': meioPagamento['meioPagamento'],
            'pagamento': meioPagamento['pagamento'],
            'taxaOperadora': meioPagamento['taxaOperadora']
        }

        return resposta

    def buscarMeioPagamento(id):
        id = int(id)
        for meioPagamento in MeioPagamentoRepositorio().buscarMeioPagamento(id):
            resposta = {
                'id': meioPagamento['_id'],
                'meioPagamento': meioPagamento['meioPagamento'],
                'pagamento': meioPagamento['pagamento'],
                'taxaOperadora': meioPagamento['taxaOperadora']
            }
            return resposta

    def listarMeioPagamentos():
        resposta = {}
        meioPagamentos = []
        for meioPagamento in MeioPagamentoRepositorio().listarMeioPagamentos():
            meioPagamento = {
                'id': meioPagamento['_id'],
                'meioPagamento': meioPagamento['meioPagamento'],
                'pagamento': meioPagamento['pagamento'],
                'taxaOperadora': meioPagamento['taxaOperadora']
            }
            meioPagamentos.append(meioPagamento)
            resposta = {
                        'meioPagamentos': meioPagamentos
                        }
        return resposta

    def deletarMeioPagamento(id):
        MeioPagamentoRepositorio().deletarMeioPagamento(id)
