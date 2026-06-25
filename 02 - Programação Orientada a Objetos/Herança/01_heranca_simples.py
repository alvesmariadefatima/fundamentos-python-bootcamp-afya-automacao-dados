class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return self.cor
    
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()

carro = Caminhao("branco", "xde-0098", 4, False)
carro.ligar_motor()
carro.esta_carregado()

caminhao = Caminhao("roxo", "gfd-8712", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)