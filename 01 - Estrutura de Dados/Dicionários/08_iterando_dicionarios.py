contatos = {
    "contato@teste.com": {"nome": "Teste 1", "telefone": "9876-5432"},
    "contato@teste2.com": {"nome": "Teste 2", "telefone": "9876-5437"},
    "contato@teste3.com": {"nome": "Teste 3", "telefone": "9876-5435"},
    "contato@teste4.com": {"nome": "Teste 4", "telefone": "9876-5434"},
}

for chave in contatos:
    print(chave, contatos[chave])

# print("#" * 100)

# for chave, valor in contatos.items():
#     print(chave, valor)