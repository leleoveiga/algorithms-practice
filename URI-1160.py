n = int(input())

for i in range(n):
    a, b, taxaA, taxaB = list(map(float, input().split()))
    int
    anos = 0
    while a <= b and anos <= 100:
        a += int(a*(taxaA/100))
        b += int(b*(taxaB/100))
        anos += 1
    if anos <= 100:
        print("%d anos." % anos)
    else:
        print("Mais de 1 seculo.")
