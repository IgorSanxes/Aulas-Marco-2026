opcao = None

while opcao != "0":
    print("1- Mostrar nome")
    print("2- Mostrar nota")
    print("3- Mostrar sistuação")
    print("0- Sair")
    opcao = input("Escolha uma Opção: ")
    if opcao == "1":
        print("Igor Sanches")
    elif opcao == "2":
        print("Sua nota é: 10")
    elif opcao == "3":
        print("Aprovado")
    elif opcao == "0":
        print("Saindo do Sistema")