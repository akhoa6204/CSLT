def delete(L,x):
    new=[]
    for i in L:  
        if i!=x:
            new+=[i]
    return new
x=int(input())
L=[]
n=int(input())
for i in range(n):
    i=int(input())
    L+=[i]
L=delete(L,x)
print(L)