n=int(input('Tong so nhap: '))
l=[]
while True: 
    i=int(input())
    l=l+[i]
    if len(l)==n:
        break
N=[]
for i in l:
    if i<0:
        N=N+[i]
for i in l:
    if i==0:
        N=N+[i]
for i in l:
    if i>0:
        N=N+[i]
print(N)