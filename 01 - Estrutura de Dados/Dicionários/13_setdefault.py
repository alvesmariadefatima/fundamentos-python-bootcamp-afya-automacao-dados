contato = {"nome": "Maria de Fátima", "telefone": "99834-3593"}

# contato.setdefault("nome", "Fátima") # "Maria de Fátima"
# print(contato) # {'nome': 'Fátima', 'telefone': 99834-3593}

contato.setdefault("idade", 25) # 25
print(contato) # {'nome': 'Fátima', 'telefone': '99834-3593', 'idade': 25}