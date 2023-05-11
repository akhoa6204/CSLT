n=str(input())
n=n.split(',')
h=[]
for i in n : 
    if int(i,2)%3==0:
        h+=[i]
print(','.join(h))