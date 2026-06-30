class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self.nro_agencia = nro_agencia
        self.saldo = saldo

    def depositar(self, valor):
        # ...
        self.saldo += valor

    def sacar(self, valor):
        # ...
        self.saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self.saldo

conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())