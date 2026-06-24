contatos = {
    "mnunesalves334@gmail.com": {"nome": "Maria de Fátima", "telefone": "998343593"},
    "joao@gmail.com": {"nome": "João", "telefone": "9876-5432"},
    "george@gmail.com": {"nome": "George", "telefone": "9675-4685"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "9856-3465"}
}

resultado = "maria@gmail.com" in contatos
print(resultado)

resultado = "joao@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["mnunesalves334@gmail.com"]
print(resultado)

resultado = "telefone" in contatos["mnunesalves334@gmail.com"]
print(resultado)
