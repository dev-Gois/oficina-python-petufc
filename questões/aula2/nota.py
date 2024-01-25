nota = int(input("Digite a nota do estudante (entre 0 e 100): "))

# Verifica se a nota está na faixa permitida
if 0 <= nota <= 100:
    # Classifica a nota usando if, elif e else
    if nota >= 90:
        print("A: Nota excelente")
    elif nota >= 80:
        print("B: Ótima nota")
    elif nota >= 70:
        print("C: Boa nota")
    elif nota >= 60:
        print("D: Nota razoável")
    elif nota >= 50:
        print("E: Nota insuficiente")
    else:
        print("F: Nota abaixo do esperado")
else:
    print("Nota inválida. Por favor, insira uma nota entre 0 e 100.")