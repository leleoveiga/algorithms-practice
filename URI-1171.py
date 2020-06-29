n = int(input())

dic = {}
for i in range(n):
    x = int(input())
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

for i in sorted(dic):
    print("%d aparece %d vez(es)" % (i, dic[i]))

#### sem dicionario ####

n = int(input())

lista = []
listaunicos = []
for i in range(n):
    x = int(input())
    lista.append(x)
    if not x in listaunicos:
        listaunicos.append(x)

for i in sorted(listaunicos):
    print("%d aparece %d vez(es)" % (i, lista.count(i)))
