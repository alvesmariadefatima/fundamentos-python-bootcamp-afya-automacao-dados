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

exp = saldo >= saque and saque <= limite and saldo >= saque

print(exp)

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente= conta_especial and saldo >= saque

exp3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp3)