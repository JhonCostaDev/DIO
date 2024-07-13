class Cliente:
    def __init__(self, _endereco, _contas, realiza_transacoes, add_conta):
        self._endereco = _endereco
        self._contas = _contas
        self.realiza_transacoes = realiza_transacoes
        self.add_conta = add_conta
        
class Pessoa_fisica(Cliente):
    def __init__(self, _endereco, _contas, realiza_transacoes, add_conta):
        super().__init__(_endereco, _contas, realiza_transacoes, add_conta)