operacao = int(input("Escolha uma operação matemática: 1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão.  "))
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if operacao == 1:
    print("Soma: ", n1 + n2)
elif operacao == 2:
    print("Subtração: ", n1 - n2)
elif operacao == 3:
    print("Multiplicação: ", n1 * n2)
elif operacao == 4:
    print("Divisão: ", n1 / n2)
else:
    print("Operação inválida!")                