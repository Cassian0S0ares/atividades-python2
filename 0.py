primeiro = int(input("Coloque o primeiro numero: "))
ultimo = int(input("Coloque o ultimo numero: "))
if primeiro < ultimo:
    for i in range (primeiro, ultimo + 1):
        print(i, end=" ")
else: 
    for i in range (primeiro, ultimo + 1, -1):
        print(i, end=" ")