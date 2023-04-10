n=int(input('n='))
L=[]
while True: 
    i=int(input())
    L=L+[i]
    if len(L)==n:
        break
s=0
for i in range(len(L)):
    if i%2!=0:
        s=s+L[i]
print('Tong=',s,sep='')