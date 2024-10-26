import random

personagens = ["Zezinho", "Luizinho", "Huguinho"]
acoes = ["correu", "dançou", "pulou"]
locais = ["escola", "discoteca", "biblioteca"]

personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)

print(f"O {personagem} do nada {acao} no meio da {local}")