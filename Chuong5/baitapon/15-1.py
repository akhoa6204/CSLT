def add(L,x,k):
    if k<n:
        L=L[:k]+[x]+L[k:]        
    else:
        L+=[x]
    return L
L=[]
n=int(input())
while True:
    i=int(input())
    L+=[i]
    if len(L)==n:
        break 
x=int(input('nhap x='))
k=int(input('nhap k='))
L=add(L,x,k)
print(L)



    
    