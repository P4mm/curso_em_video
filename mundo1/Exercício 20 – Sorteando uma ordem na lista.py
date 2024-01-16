import random

alunos = []

for i in range(4):
  nome = input("Digite o nome do aluno: ")
  alunos.append(nome)

random.shuffle(alunos)

print("Ordem de apresentação dos trabalhos:")
for aluno in alunos:
  print(aluno)
