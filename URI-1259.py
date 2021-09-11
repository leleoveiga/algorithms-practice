n = int(input())
pares = []
impares = []
for i in range(n):
    m = input()
    if int(m[-1]) % 2 == 0:
        pares.append(m)
    else:
        impares.append(m)

pares = list(map(int, pares))
pares.sort()
# print(pares)
impares = list(map(int, impares))
impares.sort(reverse=True)
# print(impares)
pares.extend(impares)
# print(pares)
for i in pares:
    print(i)