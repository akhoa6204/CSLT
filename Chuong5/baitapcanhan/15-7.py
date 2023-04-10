n=int(input('n='))
L=[]
while True: 
    i=int(input())
    L=L+[i]
    if len(L)==n:
        break
N=[]
for i in L:
    if i not in N:
        N=N+[i]
    else: continue 
print(N)

    