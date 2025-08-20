
vendas = float(input("Digite o valor das suas vendas: "))

if vendas >= 50000:
    comm = vendas * 0.12
elif 50000 > vendas > 30000:
    comm = vendas * 0.095
else:
    comm = vendas * 0.07

print(f"Você irá receber R${comm:.2f}.")