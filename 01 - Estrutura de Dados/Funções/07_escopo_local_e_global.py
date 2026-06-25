salario = 1586

def salario_bonus(bonus):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(700)
print(salario_com_bonus)
print(lista)