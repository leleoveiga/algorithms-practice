# n, meta = map(int, input().split())

# clist = list(map(int, input().split()))


def cookies(meta, cookies):
    cookies.sort(reverse=True)
    op = 0
    while len(cookies) > 1 and cookies[-1] <= meta:
        print(cookies)
        c1 = cookies.pop()
        c2 = cookies.pop()
        print(cookies)
        print(c1, c2)
        new = c1 + (2 * c2)
        print(new)
        cookies.append(new)
        cookies.sort(reverse=True)
        print(cookies)
        op += 1
    return op if op > 0 else -1

print(cookies(5, [1,1,1,1]))