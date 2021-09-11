t = int(input())

blocksTotal = []

for i in range(t):
    n, m = list(map(int,input().split()))
    blocos = list(map(int, input().split()))
    blocos.sort(reverse=True)
    total = 0
    qt = 0

    while i < len(blocos):
        # print(i)
        if (blocos[i] + total) <= m:
            total += blocos[i]
            qt += 1
        else:
            i += 1
    
    # print(total)
    print(qt)
        