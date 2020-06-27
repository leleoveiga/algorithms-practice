n = int(input())

for i in range(n):
    x = list(map(int, input().split()))
    lista = []
    for j in range(x[0]):
        lista.append(j+1)
    eliminados = 0
    j = x[1]-1
    while eliminados < x[0]-1:
        #print(j)
        #print(lista)
        
        del lista[j]
        eliminados += 1
        passadas = 0
        j += x[1]-1
        if j > len(lista)-1:
            j = j % len(lista)
    print("Case %d: %d" % (i+1, lista[0]))
