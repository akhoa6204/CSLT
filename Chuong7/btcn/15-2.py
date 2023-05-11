n=str(input()).lower()
n=n.strip().split()
c=[',',';','.',':']
a=[]
h=[]
for i in range(len(n)) : 
    if n[i] not in c : 
        h+=n[i]+' '
        if i == len(n) - 1 :
            a+=[''.join(h).strip()]
    else: 
        h=''.join(h).strip()
        a+=[''.join(h+n[i])]
        h=[]
print(' '.join(a).capitalize())

       

