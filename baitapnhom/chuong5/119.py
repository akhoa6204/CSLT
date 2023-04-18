from random import randrange
def createDeck():
    bobai=[]
    ds=['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
    nt=['s','c','d','h']
    for i in ds:
        for n in nt:
            bobai+=[''.join(str(i)+str(n))]
    return bobai 

def suffle(bobai):
    for i in range(len(bobai)):
        a=randrange(0,len(bobai))
        b=bobai[i]
        bobai[i]=bobai[a]
        bobai[a]=b
        #random bộ bài 

def chiabai(bobai):
    hs=[]
    for i in range(sotay): 
        h=[]
        for j in range(baitrentay): 
            h.append(bobai.pop(0))
        hs.append(h)
    return hs

bobai=createDeck()
print('Bộ bài ban đầu')
print(bobai)
print()

suffle(bobai)
print('Bộ bài sau khi xào bài')
print(bobai)
print()

sotay=int(input('Số Người chơi: '))
baitrentay=int(input('Số lá mỗi người có: '))
hs=chiabai(bobai)
for i in range(sotay):
    print('Người chơi',i+1)
    for bai in hs[i]:
        print(bai,end=' ')
    print()

print('Bộ bài sau khi chia')
print(bobai)
 
     
        
        
    
    

    