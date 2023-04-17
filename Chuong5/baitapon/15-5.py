def update(L,x,y):
    for i in range(len(L)):
        if L[i]==x :
            L[i]=y
    print(L)
L=[]
n=int(input())
while True:
    i=int(input())
    L+=[i]
    if len(L)==n:
        break 
x=int(input('nhap x='))
y=int(input('nhap y='))
update(L,x,y)