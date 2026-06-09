nome = "MaRia"

# exemplo de nome com letras maiúsculas, minúsculas e título
print(nome.upper())
print(nome.lower())
print(nome.title())

# exemplo de nome com espaços em branco no início e no final
texto = "Estou participando do bootcamp Afya    "
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

# exemplo de centralização de texto com preenchimento de caracteres
print("###" + menu + "###")
print(menu.center(14))
print(menu.center(20, "*"))
print("-".join(menu))

# exemplo de iteração sobre os caracteres de uma string
# for letra in menu:
#    print(letra, end="-")
#    print("-".join(menu))