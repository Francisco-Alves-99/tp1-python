numero_secreto = 6

palpite = int(input("Digite o palpite para adivinhar o número secreto: "))

if palpite == numero_secreto:
    print("seu palpite foi correto!")
elif palpite > numero_secreto:
    print("palpite foi muito alto")
elif palpite < numero_secreto:
    print("palpite foi muito baixo")        