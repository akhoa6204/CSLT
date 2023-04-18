l=list(input())
h=[]# def tachchuoi(l):
tb=['*','/','^','(',')','+','-']
n=[]
for i in range(len(l)):
    
    if l[i]=='+' and l[i+1]==' ':
        n+=[l[i]]+[l[i+1]]
        continue
    elif l[i]=='-' and l[i+1]==' ':
        n+=[l[i]]+[l[i+1]]
        continue
    if l[i] not in tb :
        n+=[l[i]]
        if i==len(l)-1:
            h+=[''.join(n)]
    else:
        if len(n)>=1:
            h+=[''.join(n)]+[l[i]]
            n=[]
        else:
            h+=[l[i]]
            n=[]

print(h)
