def delete(L,x):
    N=[]
    for i in L:
        if i!=x:
            N=N+[i]
    print(N)
   
L = [1,2,2,3,4,'a',2,3,2,5,2,2,1,1,1,2]
x = 2
delete(L,x)