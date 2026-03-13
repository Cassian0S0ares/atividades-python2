print("Urna eletronica")
vezes = 5
voto1= 0
voto2= 0
voto3= 0
voto4= 0
voto5= 0
for i in range(vezes):
    print("1. Candidato Jair Rodrigues")
    print("2. Candidato Carlos Luz")
    print("3. Candidato Neves Rocha")
    print("4. Nulo")
    print("5. Branco")
    print("6. Resultado")
    votos = input("Selecione o seu canditato: ")
    if votos == 1:
        voto1 += voto1
    elif votos == 2:
        voto2 += voto2
    elif votos == 3:
        voto3 += voto3
    elif votos == 4:
        voto4 += voto4
    elif votos == 5:
        voto5 += voto5
    else:
        votoss = [voto1, voto2, voto3, voto4, voto5]
        print(f"o resutaldo dos votos são: ")
        print(votoss.sort())
