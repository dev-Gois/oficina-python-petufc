def potencia_recursiva(base, expoente):
    # Caso base: quando o expoente é 0, o resultado é 1
    if expoente == 0:
        return 1
    # Caso recursivo: multiplicar a base pelo resultado da potência com um expoente menor
    else:
        return base * potencia_recursiva(base, expoente - 1)