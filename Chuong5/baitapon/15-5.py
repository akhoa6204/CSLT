def update(L,x,y):
    for i in L:
        if i==x :
            L[L.index(i)]=y
    print(L)
L=[1,2,3,4,3,4,5,5,3,3,2,1]
x=3
y=10 
update(L,x,y)