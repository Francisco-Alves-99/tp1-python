valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 100 and valor_compra <= 200:
    desconto = valor_compra * 10 / 100
    valor_compra -= desconto
    print("Valor da compra com 10% de desconto: ", valor_compra)
elif valor_compra > 200 and valor_compra <= 500:
    desconto = valor_compra * 15 / 100
    valor_compra -= desconto
    print("Valor da compra com 15% de desconto: ", valor_compra)
elif valor_compra > 500:
    desconto = valor_compra * 25 / 100
    valor_compra -= desconto
    print("Valor da compra com 25% de desconto: ", valor_compra)        