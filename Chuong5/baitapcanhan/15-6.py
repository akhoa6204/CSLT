L=[]
while True: 
    i=int(input())
    L=L+[i]
    if len(L)==10:
        break
N=[]
for i in range(0,len(L),2):
    N=N+[L[i+1]]
    N=N+[L[i]]
print(N)
    