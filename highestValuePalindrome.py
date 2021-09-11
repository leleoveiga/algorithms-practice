def highestValuePalindrome(s, n, k):
    i = 0
    j = n-1
    op = 0
    altered = []
    minsTotal = []
    
    s = list(map(int, s))
    print(s)
    if k == 1 and n % 2 != 0 or n == 1 and k > 0:
        s[int(n/2)] = 9
    print(s)
    while i < j and i != j:
        if s[i] != s[j]:
            s[i], s[j] = max(s[i],s[j]),  max(s[i],s[j])
            altered.append([i, s[i]])
            k -= 1
            print(k)
        minsTotal.append([i, s[i]])
        i += 1
        j -= 1
    print(altered)
    print("Olha o k", k)
    if k < 0:
        return "-1"
    minsAltered = sorted(altered, key=lambda x:x[1])
    print(minsAltered)
    
    for x in minsAltered:
        if k < 1:
            break
        s[x[0]], s[(n-x[0]-1)] = 9, 9
        k -= 1
        
    totalSorted = sorted(minsTotal, key=lambda x:x[1])
    print('dps do segundo for', s)
    print('totalSorted', totalSorted)
    for i in totalSorted:
        if k < 2:
            break
        if s[i[0]] < 9 and s[(n-i[0]-1)] < 9:
            s[i[0]], s[(n-i[0]-1)] = 9 , 9
            k -= 2
    print(s)
    return "".join(list(map(str,s)))
    

s = "3943"
n = 4
k = 1

highestValuePalindrome(s,n, k)