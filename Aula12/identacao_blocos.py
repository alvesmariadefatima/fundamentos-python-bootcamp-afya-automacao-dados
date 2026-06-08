# exemplo de identação de blocos em python
def sacar(valor):

    saldo = 1800

# exemplo de identação de blocos na estrutura condicional if
    if saldo >= valor:
        print("Valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500

    saldo += valor

sacar(2000)
depositar(1000)