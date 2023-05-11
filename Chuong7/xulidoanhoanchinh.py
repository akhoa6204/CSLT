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
           
a=' '.join(a).capitalize()
b=a.split('. ')
b=[n.capitalize() for n in b]
print('. '.join(b))

