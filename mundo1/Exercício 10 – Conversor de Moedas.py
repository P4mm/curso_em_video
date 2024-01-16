real = float(input("Digite o valor em reais: "))
cotacao_dolar = 5.50
dolar = real / cotacao_dolar

print(f"Com R${real:.2f} você pode comprar US${dolar:.2f}")
