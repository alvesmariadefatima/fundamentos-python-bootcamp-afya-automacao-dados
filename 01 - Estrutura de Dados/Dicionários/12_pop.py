contatos = {"mariadefatimanunesalves343@gmail.com": {"nome": "Maria de Fátima", "telefone": "99834-3593"}}

resultado = contatos.pop("mariadefatimanunesalves343@gmail.com") # {'nome': 'Maria de Fátima', 'telefone': '99834-3593'}
print(resultado)

resultado = contatos.pop("mariadefatimanunesalves343@gmail.com", "não encontrou") # {}
print(resultado)