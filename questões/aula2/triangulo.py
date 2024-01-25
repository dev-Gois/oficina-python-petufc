cateto1 = float(input("Digite o comprimento do cateto 1: "))
cateto2 = float(input("Digite o comprimento do cateto 2: "))
hipotenusa = float(input("Digite o comprimento da hipotenusa: "))

# Verifica se é um triângulo retângulo usando o teorema de Pitágoras
if cateto1**2 + cateto2**2 == hipotenusa**2 or cateto1**2 + hipotenusa**2 == cateto2**2 or cateto2**2 + hipotenusa**2 == cateto1**2:
    print("É um triângulo retângulo.")
else:
    print("Não é um triângulo retângulo.")