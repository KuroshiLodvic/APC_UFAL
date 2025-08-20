num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 % num2 and num2 % num1 == 0:
    print(f"{num1} e {num2} são múltiplos.")
else:
    print(f"{num1} e {num2} não são múltiplos.")