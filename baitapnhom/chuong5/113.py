l=[]
i=input()
n=['and']
while True:
    if i=='k':
        break
    l+=[i]
    i=input()
n+=[l[-1]]
del(l[-1])
l=','.join(l)+' '+' '.join(n)
print(l)
    