# texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"

# exemplo de uso do for com string
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    # Imprime uma nova linha após o loop terminar
    print()  

# exemplo de uso do for com range
for numero in range(0, 51, 5):
    print(numero, end=" ")