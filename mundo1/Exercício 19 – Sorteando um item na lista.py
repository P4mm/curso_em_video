import random

alunos = []

# Lendo o nome dos alunos
for i in range(4):
  nome = input("Digite o nome do aluno: ")
  alunos.append(nome)

# Sorteando um aluno
escolhido = random.choice(alunos)

# Exibindo o nome do aluno escolhido
print("O aluno escolhido foi:", escolhido)
