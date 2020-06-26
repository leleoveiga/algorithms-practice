while True:
    try:
        n = int(input())
        stack = 0
        queue = 0
        pqueue = 0
        impossible = False
        output = []
        # lista = []
        lista2 = []
        for i in range(n):
            flag = False
            op = list(map(int, input().split()))
            # print (op)
            if op[0] == 1:
                # lista.append(op[1])
                lista2.append(op[1])
                # print (lista2)
            elif op[0] == 2:
                if op[1] == lista2[-1]:
                    stack += 1
                    flag = True
                if op[1] == lista2[0]:
                    queue += 1
                    flag = True
                if op[1] == max(lista2):
                    pqueue += 1
                    flag = True
                if not op[1] in lista2:
                    impossible = True
                    break
                if flag:
                    lista2.remove(op[1])

            # print(stack,queue,pqueue)

        maximo = max(stack,queue,pqueue)

        if maximo == stack:
            output.append("stack")
        if maximo == queue:
            output.append("queue")
        if maximo == pqueue:
            output.append("priority queue")
        if len(output) == 0:
            impossible = True
        if not impossible:
            if len(output) > 1:
                print("not sure")
            else:
                print(output[0])
        else:
            print("impossible")

    except EOFError:
        break
