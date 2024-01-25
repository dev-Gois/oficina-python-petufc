# Dicionário inicial
pessoa = {
    'nome': 'Maria',
    'idade': 28,
    'cidade': 'São Paulo',
    'profissao': 'engenheira'
}

# a) Imprimir o nome da pessoa
print("a) Nome da pessoa:", pessoa['nome'])

# b) Adicionar a chave 'email' com o valor 'maria@email.com' ao dicionário
pessoa['email'] = 'maria@email.com'
print("b) Dicionário após adicionar o email:", pessoa)

# c) Atualizar a idade para 29
pessoa['idade'] = 29
print("c) Dicionário após atualizar a idade:", pessoa)