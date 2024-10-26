texto = input("Digite uma palavra ou uma frase: ")

textoVeriicado = texto.replace(" ", "").lower()

if textoVeriicado == textoVeriicado[::-1]:
    print("é um palíndromo")
else:
    print("não é um palíndromo")    