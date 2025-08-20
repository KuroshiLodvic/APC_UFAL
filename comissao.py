
sal = float(input("Digite o seu salário fixo: "))
vendas = int(input("Quantos carros você vendeu? "))
venda_total = float(input("Qual foi o valor total de suas vendas? "))
com_venda = float(input("Quanto você recebe por venda? "))

sal_total = sal + (com_venda * vendas) + (venda_total * 0.05)

print(f"Você receberá R${sal_total}.")