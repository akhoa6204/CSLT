def count(L):
    for i in range(len(L)):
        s=i+1
    return s
L=[]
n=int(input())
while True:
    i=int(input())
    L+=[i]
    if len(L)==n:
        break
L=count(L)
print(L)