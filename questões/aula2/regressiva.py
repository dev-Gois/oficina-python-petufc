numero = int(input("Digite um número inteiro: "))

# Verifica se o número é positivo
if numero > 0:
    # Utiliza um loop for com range para exibir a contagem regressiva
    for i in range(numero, 0, -1):
        print(i)
else:
    print("Por favor, insira um número inteiro positivo.")