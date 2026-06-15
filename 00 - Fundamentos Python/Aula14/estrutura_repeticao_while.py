opcao = -1

# exemplo de estrutura de repetição com while
while opcao >= 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[3] Sair \n"))

# estrutura de decisão dentro da estrutura de repetição
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
    else:
        print("Obrigado por usar nosso sistema bancário, até logo!")