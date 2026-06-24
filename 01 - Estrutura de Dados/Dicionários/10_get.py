contatos = {"mariadefatimanunesalves343@gmail.com": {"nome": "Maria de Fátima", "telefone": "99834-3593"}}

# contatos["chave"] # KeyError

resultado = contatos.get("chave") # {}
print(resultado)

resultado = contatos.get("chave", {})
print(resultado)

resultado = contatos.get(
    "mariadefatimanunesalves343@gmail.com", {}
) # {mariadefatimanunesalves343@gmail.com: {"nome": "Maria de Fátima", "telefone": 99834-3593}}

print(resultado)