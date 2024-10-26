import random

num_dados = int(input("Digite quantos dados você quer jogar: "))

resultados = []

for _ in range(num_dados):
    resultado = random.randint(1, 6)
    resultados.append(resultado)

print("Resultado dos lançamentos: ", resultados)