peso = float(input("Digite o seu peso: ex: (92.5) "))
altura = float(input("Digite a sua altura: (ex: 1.80) "))

imc = peso / (altura * altura)

if imc <= 18.49:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc <= 24.99:
    print("Peso normal.")
elif imc >= 25:
    print("Acima do peso.")        
