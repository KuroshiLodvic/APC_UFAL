num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro: "))
num3 = float(input("Agora digite o último número: "))

if num1 > num2 > num3:
    print(f"{num1} > {num2} > {num3}")
elif num1 > num3 > num2:
    print(f"{num1} > {num3} > {num2}")

elif num2 > num1 > num3:
    print(f"{num2} > {num1} > {num3}")
elif num2 > num3 > num1:
    print(f"{num2} > {num3} > {num2}")
    
elif num3 > num1 > num2:
    print(f"{num3} > {num1} > {num2}")
else:
    print(f"{num3} > {num2} > {num1}")
