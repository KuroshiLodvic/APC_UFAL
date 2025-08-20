multa = 2
taxa = 0.05
boleto = float(input("Quanto custa o boleto? "))
atraso = input("O boleto está atrasdo? S/N ")

if atraso == "s":
    dias = int(input("Com quantos dias o boleto está com atraso? "))

    total = boleto + multa + (boleto * taxa * dias)

    print(f"Seu boleto de R${boleto:.2f} agora é de R${total:.2f}.")

else:
    print(f"Como você está dentro do prazo, você irá pagar apenas R${boleto:.2f}.")