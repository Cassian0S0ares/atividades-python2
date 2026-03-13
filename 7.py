numero = int(input("Digite um número: "))
for i in range(numero, 1, -1):
    numero = numero * (i - 1)
print(f"O resultado é: {numero}")