n=str(input())
n=n.split()
n=[int(a) for a in n]
i=int(input())
a=1
if i not in n:
    print('0')
else: 
    for h in range (len(n)):
        if i in n : 
            print(n.index(i)+a)
            a+=1
            n.remove(i)
