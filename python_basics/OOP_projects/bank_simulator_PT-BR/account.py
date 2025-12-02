class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = float(saldo_inicial)

        print(f'Conta criada para {self.titular} com saldo de R${self._saldo:.2f}. ')

    def depositar(self, valor):
        valor = float(valor)
        if valor > 0:
            self._saldo += valor
            print(f'Depósito de R${valor:.2f} realizado. ')
            self.ver_saldo()
        else:
            print('Valor de depósito inválido, valor deve ser positivo. ')
        
    def sacar(self, valor):
        valor = float(valor)
        if valor <= 0:
            print('Valor de saque inválido, valor deve ser positivo. ')
        elif valor > self._saldo:
            print(f'Saldo insuficiente, você tem R${self._saldo:.2f}, mas tentou sacar R${valor:.2f}. ')
        else:
            self._saldo -= valor
            print(f'Saque de {valor:.2f}, realizado com sucesso. ')
            self.ver_saldo()

    def ver_saldo(self):
        print(f'Saldo atual de {self.titular} igual a, R${self._saldo:.2f}. ')