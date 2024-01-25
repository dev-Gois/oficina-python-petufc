# Dicionário de notas de alunos
notas_alunos = {
    'João': 85,
    'Maria': 92,
    'Pedro': 78,
    'Ana': 95
}

# a) Loop para imprimir os nomes dos alunos
print("a) Nomes dos alunos:")
for aluno in notas_alunos:
    print(aluno)

# b) Loop para imprimir os nomes dos alunos e suas respectivas notas
print("\nb) Nomes dos alunos e suas notas:")
for aluno, nota in notas_alunos.items():
    print(f"{aluno}: {nota}")