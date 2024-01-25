lista_numeros = []

while True:
    print("\nOperações disponíveis:")
    print("1 - Adicionar número")
    print("2 - Remover número")
    print("3 - Sair")

    escolha = input("Escolha uma operação (1/2/3): ")

    if escolha == "1":
        numero = int(input("Digite o número a ser adicionado: "))
        lista_numeros.append(numero)
        print(f"Número {numero} adicionado à lista.")
    elif escolha == "2":
        if not lista_numeros:
            print("A lista está vazia. Não há números para remover.")
        else:
            print("Lista atual:", lista_numeros)
            posicao = int(input("Digite a posição do número a ser removido: "))
            if 0 <= posicao < len(lista_numeros):
                numero_removido = lista_numeros.pop(posicao)
                print(f"Número {numero_removido} removido da lista.")
            else:
                print("Posição inválida. Tente novamente.")
    elif escolha == "3":
        print("Lista final:", lista_numeros)
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
