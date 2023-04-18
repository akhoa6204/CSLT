i=str(input())
i=i.lower()
l=list(i)
k=['u','o','e','a','i','y']
h=['!','.','?',',']
if l[0] in k : 
    if l[-1] in h : 
        N=l[:-1]
        N.append('way'+l[-1])
        l=''.join(N)   
        l=l.capitalize()
        print(l)
    else: 
        l.append('way')
        l=''.join(l)
        l=l.capitalize()
        print(l)
else:   
    for n in range(1,len(l)) :  
        if l[-1] not in h:    
            if l[n] in k: 
                N=l[n:]+l[:n]
                N.append('ay')
                l=''.join(N)   
                l=l.capitalize()
                print(l)
                break 
        else:   
            if l[n] in k:
                N=l[n:-1]+l[:n]
                N.append('ay'+l[-1])
                N=''.join(N)   
                N=N.capitalize()
                print(N)
                break
    
    
            
    
    