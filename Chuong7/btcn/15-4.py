n=str(input())
n=n.split(',')
h=[]
for i in n : 
    if i not in h:
        h.append(i)
h.sort()
print(','.join(h))