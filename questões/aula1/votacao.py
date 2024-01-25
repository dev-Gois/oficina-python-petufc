idade = int(input("Digite sua idade: "))
brasileiro = input("Você é brasileiro? (Digite 'sim' ou 'nao'): ").lower()

elegivel_para_votacao = idade >= 16 and brasileiro == 'sim'

print("Elegível para votação:", elegivel_para_votacao)