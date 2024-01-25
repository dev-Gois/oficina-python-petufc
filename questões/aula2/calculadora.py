while True:
    print("\nOpções:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    # Solicita ao usuário escolher uma opção
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '5':
        print("Saindo da calculadora. Até mais!")
        break

    # Solicita os números para a operação
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    # Executa a operação escolhida
    if opcao == '1':
        resultado = numero1 + numero2
        print(f"Resultado da soma: {resultado}")
    elif opcao == '2':
        resultado = numero1 - numero2
        print(f"Resultado da subtração: {resultado}")
    elif opcao == '3':
        resultado = numero1 * numero2
        print(f"Resultado da multiplicação: {resultado}")
    elif opcao == '4':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Erro: divisão por zero")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")