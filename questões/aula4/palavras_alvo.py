def palavras_contendo_alvo(lista_palavras, palavra_alvo):
    palavras_encontradas = []
    for palavra in lista_palavras:
        if palavra_alvo in palavra:
            palavras_encontradas.append(palavra)
    return palavras_encontradas