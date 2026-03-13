import random
quantiedade = int(input("Digite a quantiedade de vezes a moeda vai ser girada: "))
moedas_giradas = 0
for i in range(quantiedade):
    resultado = random.randint(0, 1)
    if resultado == 0:
        print("Cara")
        moedas_giradas == moedas_giradas + 1
    else:
        print("Coroa")
        moedas_giradas == moedas_giradas + 1
