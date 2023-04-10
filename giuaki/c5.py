n=int(input())
if 1<=n<=106:
    s=0
    for i in range (1,n+1):
        if i%2==0:
            s=s+i
    print(s)