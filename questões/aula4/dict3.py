# Dicionários fornecidos
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'c': 10, 'd': 4, 'e': 5}

# a) Criar um novo dicionário que seja a união de dicionario1 e dicionario2
novo_dicionario = {**dicionario1, **dicionario2}
print("a) Novo dicionário (união de dicionario1 e dicionario2):", novo_dicionario)

# b) Remover a chave 'b' do novo dicionário
if 'b' in novo_dicionario:
    del novo_dicionario['b']
    print("b) Novo dicionário após remover a chave 'b':", novo_dicionario)
else:
    print("b) A chave 'b' não está presente no novo dicionário.")

# c) Calcular a soma dos valores no novo dicionário
soma_valores = sum(novo_dicionario.values())
print("c) Soma dos valores no novo dicionário:", soma_valores)