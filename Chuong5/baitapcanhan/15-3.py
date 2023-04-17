n=int(input('n='))
L=[]
while True: 
    i=int(input())
    L=L+[i]
    if len(L)==n:
        break
snd=0
sl=0
s=0
for i in range(len(L)):
    if L[i]>0:
        snd+=1
    if L[i]%2==0:
        sl+=1
        s=s+L[i]
if sl==0:tbc=0
else: tbc=s/sl 
print('SND=',snd,sep='')
print('TBC=',tbc,sep='')
        
