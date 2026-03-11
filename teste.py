nota1 = float(input("Digite a Primeira Nota: "))
nota2 = float(input("Digite a Segunda Nota: "))

media = (nota1 + nota2)/2

if media >= 5:
    print("Aprovado!!!")
elif media >=4:
    print("Recuperção")
else:
    print("Reprovado")