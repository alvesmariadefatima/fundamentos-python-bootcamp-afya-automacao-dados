# AND = para ser True tudo tem que ser True
# OR = para ser True pelo menos um tem que ser True

print(True and True and True)
print(True and False and True)
print(True or True or True)
print(True or False or True)

saldo = 1586
saque = 900
limite = 500
conta_especial = True

# exemplo de expressão com operador lógico and
exp = saldo >= saque and saque <= limite and saldo >= saque

print(exp)

# exemplo de expressão com operadores lógicos and e or
exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)

# exemplo de expressão com operadores lógicos and e or utilizando variáveis intermediárias para verificar se as contas normal e especial estão com saldo suficiente para o saque
conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente= conta_especial and saldo >= saque

# expressão utilizando as variáveis intermediárias se as contas normal e especial estão com saldo suficiente para o saque
exp3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp3)