senha_cadastrada = "123"
senha_digitada = input("Digite a sua senha: ")

while senha_cadastrada != senha_digitada:
    print ("Senha incorreta, tente novamente!")
    senha_digitada = input("Digite a sua senha:")
print("Login efetuado com sucesso")