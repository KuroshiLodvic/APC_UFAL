print("-" * 5, "Calculadora gaymer", "-" * 5)

n1 = int(input("Digite o número que você quer multiplicar: "))
n2 = int(input("Digite o número que você vai querer que multiplique: "))

for i in range(10):
    print(f"{n1} * {n2} = {n1 * n2}")
    n2 += 1