i=str(input())
l=list(i)
k=['u','e','o','a','i','y']
if l[0] in k: 
    print(i+'way',sep='')
else:   
    for n in range(1,len(l)) :  
        if l[n] in k: 
            N=l[n:]+l[:n]
            break 
    N.append('ay')
    l=''.join(N)   
    print(l )
  
