#Desconto de 5% para valores acima de 30
valores = [4.50, 10, 19.50, 35, 50]

for valor in valores:
    if valor >= 30:
        print(valor * 0.95)
    else:
        print(valor)