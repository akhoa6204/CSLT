def Input():
    n=int(input('n='))
    L=[]
    while True: 
        i=int(input())
        L=L+[i]
        if len(L)==n:
            break
    x=int(input('x='))
    return n,L,x       
def FirstandLast(L):
    N=[]
    for i in range (len (L)) :
        if i==0:
           N=N+[L[0]]
        if i==len(L)-1: 
            N=N+[L[-1]]
    print(N)
def Search(L,x):
    if x not in L:
        return False
    else: return True

n,L,x=Input()
FirstandLast(L)
print(Search(L,x))
