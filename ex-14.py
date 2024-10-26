voto = int(input("Vote em uma das 3 opcoes: 1 - opcao 1, 2 - opcao 2, 3 - opcao 3 "))

opcao1 = 0
opcao2 = 0
opcao3 = 0

if voto == 1:
    opcao1 += 1
elif voto == 2:
    opcao2 += 1
elif voto == 3:
    opcao3 += 1

print(f"Resultado: opcao 1 : {opcao1} voto(s), opcao 2: {opcao2} voto(s), opcao 3: {opcao3} voto(s)")            