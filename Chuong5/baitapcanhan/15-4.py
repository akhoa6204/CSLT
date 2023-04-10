n=int(input('n='))
L=[]
while True: 
    i=int(input())
    L=L+[i]
    if len(L)==n:
        break
L.reverse()
print(L)
L.sort()
print(L)