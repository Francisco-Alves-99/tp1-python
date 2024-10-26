minutos = int(input("Digite a quantidade de minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print(f"{minutos} minutos são {horas} horas e {minutos_restantes} minutos.")

horas_para_minutos = horas * 60 + minutos_restantes

print (f"{horas} horas e {minutos_restantes} minutos é igual a {horas_para_minutos} minutos")