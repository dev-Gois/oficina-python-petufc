import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas_maximas = 3
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar um número entre 1 e 10.")

    tentativa_atual = 1
    while tentativa_atual <= tentativas_maximas:
        # Solicitar uma tentativa ao usuário
        tentativa_str = input(f"Tentativa {tentativa_atual}: Digite sua resposta: ")

        # Verificar se a entrada é um número
        if tentativa_str.isdigit():
            tentativa = int(tentativa_str)

            # Verificar se a tentativa é igual ao número secreto
            if tentativa == numero_secreto:
                print("Parabéns! Você acertou!")
                break
            else:
                print("Tente novamente.")
                tentativa_atual += 1
        else:
            print("Por favor, digite um número válido.")

    else:
        # Se o loop for concluído sem acerto
        print(f"Fim do jogo. O número secreto era {numero_secreto}.")

# Executar o jogo
jogo_adivinhacao()