def add(L,x,k):
    if k<n:
        L=L[:k]+[x]+L[k:]        
    else:
        L+=[x]
    return L
L=[]
n=int(input())
for i in range(n):
    i=int(input())
    L+=[i]
   
x=int(input('nhap x='))
k=int(input('nhap k='))
L=add(L,x,k)
print(L)



    
    