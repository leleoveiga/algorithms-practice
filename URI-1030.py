n = int(input())

for i in range(n):
    x = list(map(int, input().split()))
    lista = []
    for j in range(x[0]):
        lista.append(j+1)
    j = 0
    while len(lista) > 1:
        j = (j+x[1]-1) % len(lista)
        del lista[j]
    print("Case %d: %d" % (i+1, lista[0]))
