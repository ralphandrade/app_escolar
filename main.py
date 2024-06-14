# Função para calcular a média e verificar se o aluno está aprovado
def calcular_media(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    return media, situacao

# Lista para armazenar os nomes dos alunos aprovados
aprovados = []

# Cadastro dos alunos
alunos = []
for i in range(5):
    nome = input("Digite o nome do aluno {}: ".format(i+1))
    notas = []
    for j in range(30):
        nota = float(input("Digite a {}ª nota do aluno {}: ".format(j+1, nome)))
        notas.append(nota)
    alunos.append((nome, notas))

# Calcular média e verificar situação de cada aluno
print("\nResultados:")
for aluno in alunos:
    nome = aluno[0]
    notas = aluno[1]
    media, situacao = calcular_media(notas)
    print("Aluno:", nome)
    print("Média:", media)
    print("Situação:", situacao)
    print()
    if situacao == "Aprovado":
        aprovados.append(nome)

# Mostrar lista de alunos aprovados
print("Alunos aprovados:")
for aluno in aprovados:
    print(aluno)