while True:
  try:
    a,b,c = list(map(int, input().split()))

    if a != b and b == c:
        print("A")
    elif b != a and a == c:
        print("B")
    elif c != b and b == a:
        print("C")
    else:
        print("*")
  except EOFError:
    break
