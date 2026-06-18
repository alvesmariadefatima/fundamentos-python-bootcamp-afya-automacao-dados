contatos = {
    "mnunesalves334@gmail.com": {"nome": "Maria de Fátima", "telefone": "99834-3593"},
    "mariadefatimanunesalves@gmail.com": {"nome": "Fátima", "telefone": "3333-3333"}
}

# exemplo de filtro de dado em um dicionário extraindo email e telefone
telefone = contatos["mnunesalves334@gmail.com"]["telefone"]
print(telefone)

extra = contatos["mnunesalves334@gmail.com"]
print(extra)
