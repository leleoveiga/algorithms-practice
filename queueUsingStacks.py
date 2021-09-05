def peek():
    if len(s2) == 0:
        while(len(s1)>0):
            s2.append(s1.pop())
        if len(s2) > 0:
            res = s2.pop()
            s2.append(res)
            return res
        else:
            return None
    else:
        return s2[-1]         
        
def enqueue(el):
    s1.append(el)

def dequeue():
    if len(s2) == 0:
        while(len(s1)>0):
            s2.append(s1.pop())
    return s2.pop() if len(s2) > 0 or len(s1) > 0 else None

n = int(input())
s1 = []
s2 = []

for i in range(n):
    query = input().split()
    if len(query) > 1:
        enqueue(int(query[1]))
    elif(query[0] == "2"):
        dequeue()
    else:
        print(peek())


for i in range(n):
    query = input().split()
    if len(query) > 1:
        enqueue(int(query[1]))
    elif(query[0] == "2"):
        dequeue()
    else:
        print(peek())


# enqueue(1)
# enqueue(2)
# print(dequeue())
# enqueue(3)
# enqueue(4)
# print(dequeue())

# for i in range(len(s1)):
#     print(dequeue())