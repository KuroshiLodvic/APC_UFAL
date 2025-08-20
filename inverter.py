numeros = int(input("digite seus números 4 (quatro) números: "))

m = numeros // 1000
numeros = numeros % 1000

c = numeros // 100
numeros = numeros % 100

d = numeros // 10
numeros = numeros % 10

u = numeros

print(f"{u}{d}{c}{m}")