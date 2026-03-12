notas = [1, 2, 3, 4, 5, 6, 7]

for indice, nota in enumerate(notas):
    if nota >= 5:
        print(f"Aluno {indice} nota:{nota} - Aprovado")
    else:
        print(f"Aluno {indice} nota:{nota} - Reprovado")