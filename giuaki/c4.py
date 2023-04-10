n=int(input())
  
if n>=100:
    n=n%100
    i=n%10
    j=n//10
    print(i+j)
else:
    print('0')
            
    