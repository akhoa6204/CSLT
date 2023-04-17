def delete(L,x):
    new=[]
    for i in L:  
        if i!=x:
            new+=[i]
    return new
L=[]
n=int(input())
while True:
    i=int(input())
    L+=[i]
    if len(L)==n:
        break
x=int(input('nhap x='))
L=delete(L,x)
print(L)