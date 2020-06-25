n = int(input())

focar = [0, 0, 0, 0]

for i in range(n):
    palpites = []
    vencedores = []
    ent = input()
    for i in range(4):
        ent = input()
        palpites.append(ent)
    ent = input()
    for i in range(4):
        ent = input()
        vencedores.append(ent)

    for i in range(len(palpites)):
        if palpites[i] == vencedores[i]:
            focar[i] += 1

# print(focar)
output = ""

m = focar[0]
for i in range(len(focar)):
    if focar[i] < focar[m]:
        m = focar[i]

for i in range(len(focar)):
    if focar[i] == m:
        output += str(i + 1) + " "

print(output.strip())