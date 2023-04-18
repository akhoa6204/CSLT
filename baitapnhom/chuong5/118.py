#2-9,T,J,Q,K,A
#bích: s 
#chuồn: c
#rô: d
#cơ: h
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
def xaobai():
    bobai=createDeck()
    print('Bộ bài ban đầu')
    print(bobai)
    print()
    suffle(bobai)
    print('Bộ bài sau khi xào bài')
    print(bobai)
    
xaobai()
    