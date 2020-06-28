while True:
  try:
    fodase = input()

    lista = list(map(int, input().split()))

    maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]

    if maior < 10:
        print(1)
    elif maior < 20:
        print(2)
    else:
        print(3)
  except EOFError:
    break
