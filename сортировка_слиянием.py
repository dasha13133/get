def merge(L, R):
    a = [0] * (len(L) + len(R))

    if L == []:
        return(R)

    elif R == []:
        return(L)

    else:
        for i in range(len(L)):
            a[i] += L[i]
        for i in range(len(R)):
            a[i+len(L)] += R[i]

    l = len(a)
    i = 0

    def func():
        for _ in range(l-1):
            if a[_] > a[_+1]:
                return(False)

    while func() == False:
        while i < l-1:
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                i = 0
                continue
            else:
                i += 1

    return(a)
print(merge([1, 3, 4, 5], [2, 3, 7]))
