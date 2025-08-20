idade = int(input("Digite sua idade: "))

if idade < 14:
    print("Você é uma criança.")
elif idade <= 17:
    print("Você é um adolescente.")
elif 59 >= idade >= 18:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")