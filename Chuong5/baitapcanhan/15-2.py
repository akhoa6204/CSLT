def Input():
    n=int(input('n='))
    L=[]
    while True: 
        i=int(input())
        L=L+[i]
        if len(L)==n:
            break
    return L
def Search(L):
    min=L[0]
    max=L[0]
    for i in range(len(L)):
        if max<L[i]:
            max=L[i]
        if min>L[i]:
            min=L[i]
    return max,min
def Output(max,min):
    print(max,min)

L=Input()
max,min=Search(L)
Output(max,min)
         