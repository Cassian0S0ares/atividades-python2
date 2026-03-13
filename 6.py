capital = int(input("Digite o valor do capital: "))
taxa = 0.5
tempo = 12
for i in range(tempo):
    montante = capital * (1 + taxa / 100) ** (i + 1)
    print(f"Valor do capital no mês {i + 1}: {montante:.2f}")