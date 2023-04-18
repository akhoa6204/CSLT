L=[]
N=[]
while True: 
    i=input()
    L=L+[i]
    if i=='':
        break
    for i in L:
        if i not in N:
            N=N+[i]
print(N)
    