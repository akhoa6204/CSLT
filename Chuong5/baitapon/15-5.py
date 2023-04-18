def update(L,x,y):
    for i in range(len(L)):
        if L[i]==x :
            L[i]=y
    print(L)
x=int(input())
y=int(input())
L=[]
n=int(input())
for i in range(n):
    i=int(input())
    L+=[i]
update(L,x,y)