dias = int(input())
custo = int(input())
lista = []

for i in range(dias):
    lista.append(int(input())-custo)

maior = 0

for i in range(dias):
    soma = 0
    for j in range(i, dias):
        soma += lista[j]
        if soma > maior:
            maior = soma


print(maior)
