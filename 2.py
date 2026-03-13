import random
numero = random.randint(1, 100)
tentativas = 3
while tentativas != 0:
    chute = int(input("Coloque o seu chute: "))
    if chute > numero:
        print(f"O seu chute {chute} foi maior que o numero secreto")
        tentativas = tentativas -1
        print(f"Você tem {tentativas} tentativas")
    elif chute < numero:
        print(f"O seu chute {chute} foi menor que o numero secreto")
        tentativas = tentativas -1
    elif chute == numero:
        print("Parabéns vc acertou o numero secreto")
        break
print(f"Você perdeu o número secreto era {numero}")