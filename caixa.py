caixa = int(input("Digite quanto você quer sacar: "))

nota100 = caixa // 100
caixa = caixa % 100

nota50 = caixa // 50
caixa = caixa % 50

nota10 = caixa // 10
caixa = caixa % 10

nota5 = caixa // 5
caixa = caixa % 5

nota1 = caixa // 1

print(f"Você irá sacar {nota100} notas de 100, {nota50} notas de 50, {nota10} notas de 10, {nota5} notas de 5 e {nota1} notas de 1.")