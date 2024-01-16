# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Exibe a tabuada do número informado
for i in range(1, 11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")
