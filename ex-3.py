n1 = input("Digite o primeiro nome: ")
n2 = input("Digite o segundo nome: ")

metade1 = n1[:len(n1) // 2]
metade2 = n2[len(n2) // 2:]

novo_nome = metade1 + metade2

print(f"{novo_nome}")