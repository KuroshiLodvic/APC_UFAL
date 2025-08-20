dolar = float(input("Digite o valor em dólares: "))
taxa_cambio = float(input("Digite a taxa de câmbio do dia: "))

real = dolar * taxa_cambio

print(f"{dolar:.2f}$ em real equivale a: R${real:.2f}")