# exemplo de estrutura de repetição com break
while True:
    numero = int(input("Informe um número: "))

# exemplo de uso do break para sair do loop quando a opção for 10
    if numero % 2 == 0:
        continue
    
    if numero == 10:
        break

# exemplo de uso do continue para pular a iteração quando a opção for 5
    print(numero)

# exemplo de uso do continue para pular a iteração quando o número for par
#for numero in range(100):
#    if numero % 2 == 0:
#        continue

#    print(numero, end=" ")