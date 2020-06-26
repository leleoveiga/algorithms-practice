x = int(input())

saida = []

while len(saida) < 6:
    if x % 2 != 0:
        saida.append(x)
    x += 1

for i in saida:
    print(i)
