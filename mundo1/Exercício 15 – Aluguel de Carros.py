# Solicita a quantidade de quilômetros percorridos
quilometros_percorridos = float(input("Quantos quilômetros foram percorridos? "))

# Solicita a quantidade de dias de aluguel
dias_aluguel = int(input("Quantos dias o carro foi alugado? "))

# Calcula o preço total a ser pago
preco_diario = 60
preco_por_km = 0.15
preco_total = (dias_aluguel * preco_diario) + (quilometros_percorridos * preco_por_km)

# Exibe o preço total a ser pago
print("O preço total a ser pago é R$", preco_total)
