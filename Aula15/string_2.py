nome = "Maria de Fátima"
idade = 25
profissao = "Desenvolvedora Backend Junior"
linguagem ="Python"
saldo = 1586

dados = {"nome": nome, "idade": idade, "profissao": profissao, "linguagem": linguagem, "saldo": saldo}

# exemplos de formatação de string usando os operadores de formatação e o método format
print("Nome: %s Idade: %d"% (nome, idade))
print("Nome: {0} Idade {1}", format(nome, idade))
print("Nome: {name} Idade {age}", format(name=nome, age=idade))
print("Nome: {name} Idade {age} {name} {age}", format(name=nome, age=idade))
print("Nome : {nome} Idade: {idade} Saldo: {saldo}", format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo: .2f}")