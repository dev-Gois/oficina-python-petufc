def soma_elementos_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma