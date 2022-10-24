while(True):
    sua, mae = input().split()
    if sua == mae == '0':
        break
    a = input().split()
    b = input().split()
    
    a = set(a)
    b = set(b)

    menor = a
    maior = b

    if len(a) > len(b):
        menor, maior = b, a    
    
    cont = 0
    for i in menor:
        if i not in maior:
            cont += 1
    
    print(cont)