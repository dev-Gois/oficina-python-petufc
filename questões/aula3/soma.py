def soma_algarismos(numero):
    # Caso base: quando o número é zero, a soma é zero
    if numero == 0:
        return 0
    # Caso recursivo: somar o último dígito com a soma dos dígitos restantes
    else:
        return numero % 10 + soma_algarismos(numero // 10)