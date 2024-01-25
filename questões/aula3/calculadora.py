def calculadora(num1, num2, operacao):
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        # Verifica se o divisor não é zero antes de realizar a divisão
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida. Por favor, use '+', '-', '*' ou '/'."

    return resultado