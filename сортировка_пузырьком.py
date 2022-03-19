a=list(map(int, input().split()))
n=len(a)
print(*a)
for i in range (n):
    for k in range(n-i-1):
        if a[k]>a[k+1]:
            a[k],a[k+1]=a[k+1],a[k]
            print(*a)
    
