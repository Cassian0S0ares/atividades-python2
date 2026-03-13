numero = int(input("Digite um numero: "))
while numero > -1:
    ultimonumero = int(input("Digite um numero: "))
    numero = numero + ultimonumero
    print(f"O resultado da soma é {numero}")
    if ultimonumero < 0:
        print("cancelado")
