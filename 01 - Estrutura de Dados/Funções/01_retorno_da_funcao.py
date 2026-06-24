def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([19, 40, 60])) # 119
print(retorna_antecessor_e_sucessor(9)) # (8, 10)