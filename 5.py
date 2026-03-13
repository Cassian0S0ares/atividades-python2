import time
print("Urna eletronica")
lista = [0, 0, 0, 0, 0]
while True:
    print("1. Candidato Jair Rodrigues")
    print("2. Candidato Carlos Luz")
    print("3. Candidato Neves Rocha")
    print("4. Nulo")
    print("5. Branco")
    print("6. Resultado")
    votos = input("Selecione o seu candidato: ")
    print(f"Você digitou: {votos}")
    if votos == "1":
        lista[0] += 1
    elif votos == "2":
        lista[1] += 1
    elif votos == "3":
        lista[2] += 1
    elif votos == "4":
        lista[3] += 1
    elif votos == "5":
        lista[4] += 1
    elif votos == "6":
        print(f"o resultado dos votos são: ")   
        print(f"Jair Rodrigues: {lista[0]} votos")
        print(f"Carlos Luz: {lista[1]} votos")
        print(f"Neves Rocha: {lista[2]} votos")
        print(f"Nulo: {lista[3]} votos")
        print(f"Branco: {lista[4]} votos")
        time.sleep(0.5)
        indice = lista.index(max(lista))
        porcetagemnulo = (lista[3] / sum(lista)) * 100
        porcetagembranco = (lista[4] / sum(lista)) * 100
        if indice == 0:
            print("O vencedor é Jair Rodrigues")
            break
        elif indice == 1:
            print("O vencedor é Carlos Luz")
            break
        elif indice == 2:
            print("O vencedor é Neves Rocha")
            break
        elif indice == 3:
            print("O vencedor é Nulo")
            print(f"Porcentagem de votos nulos: {porcetagemnulo:.2f}%")
            print("Refazer a votação")
            continue
        elif indice == 4:
            print("O vencedor é Branco")
            print(f"Porcentagem de votos brancos: {porcetagembranco:.2f}%")
            continue
    else:
        print("Escolha uma opção válida")