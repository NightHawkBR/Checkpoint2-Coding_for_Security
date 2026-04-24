# TESTE
# alunos = [("Carlos", 8.5),
#        ("Ana", 9.2),
#         ("Bruno", 6.0),
#         ("Diana", 7.8),
#         ("Eduarado", 4.5)
# ]


# Lista que armazenará as tuplas (nome, nota) de cada aluno
alunos = []

print("---| REGISTRO DE NOTAS DA TURMA |---")

# Laço para coletar os dados dos alunos
for i in range(1, 6):
    print(f"Aluno {i}:")

    nome = input(" Nome: ")
    nota = float(input(" Nota: "))

    #Criando tupla com o par (nome, nota)  e adicionando a lista
    alunos.append((nome, nota))

# Cálculo das estatísticas

# Inicializa maior e menor com a primeira tupla para te um ponto de comparação
maior = alunos[0]
menor = alunos[0]

#Acumulador para somar as notas e calcular a média
soma = 0

# Encontrando maior, menor e soma na lista de tuplas
for nome, nota in alunos:
    if nota > maior[1]:
        maior = (nome, nota)

    if nota < menor[1]:
        menor = (nome, nota)

    soma += nota

media = soma / len(alunos)

# Exibindo os resultados
print("---| RELATÓRIO DE NOTAS |---")

# Aluno com maior nota
print(f"Maior nota: {maior[1]:.1f} {maior[0]}")

# Aluno com menor nota
print(f"Menor nota: {menor[1]:.1f} {menor[0]}")

# Média da sala exibida em 2 casas decimais
print(f"Média da turma: {media:.2f}")

# Alunos acima das média
print(f"\nAlunos acima da média ({media:.2f})")

# Percorre novamente a lista para verificar quem está acima da média
acima_da_media = False
for nome, nota in alunos:
    if nota > media:
        print(f"  → {nome}: {nota:.1f}")
        acima_da_media = True

# Caso nenhum aluno esteja acima da média (todos empatados, por exemplo)
if not acima_da_media:
    print("  Nenhum aluno está acima da média.")
