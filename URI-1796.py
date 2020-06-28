fodase  = int(input())

pessoas = list(map(int, input().split()))
votos = 0
for i in range(fodase):
    if pessoas[i] == 0:
        votos += 1

if votos > int(len(pessoas)/2):
    print("Y")
else:
    print("N")
