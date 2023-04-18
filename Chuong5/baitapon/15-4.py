def count(L):
    s=0
    for i in range(len(L)):
        s=s+1
    return s
L=[]
n=int(input())
for i in range(n):
    i=int(input())
    L+=[i]
   
L=count(L)
print(L)