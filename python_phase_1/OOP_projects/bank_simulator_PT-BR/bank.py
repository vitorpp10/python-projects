from account import ContaBancaria

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []
        print(f'Bem-vindo ao {self.nome}! ')

    def abrir_conta(self, titular, saldo_inicial=0):
        if self.buscar_conta(titular):
            print(f'ERRO: {titular} ja possui uma conta neste banco. ')
            return None
    
        nova_conta = ContaBancaria(titular, saldo_inicial)
        self.contas.append(nova_conta)
        return nova_conta
    
    def buscar_conta(self, titular):
        for conta in self.contas:
            if conta.titular.lower() == titular.lower():
                return conta
            return None