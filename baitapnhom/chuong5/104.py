l=[]
while True:
    i=int(input())
    if i == 0:
        break 
    else: l=l+[i]

l.sort()
print(l)