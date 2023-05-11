n=str(input())
hoa=0
thuong=0
so=0
khac=0
for i in n : 
    if i.isupper():
        hoa+=1
    elif i.islower():
        thuong+=1
    elif i.isnumeric():
        so+=1
    else: khac+=1
print('In hoa:',hoa)
print('In thuong:',thuong)
print('Chu so:',so)
print('Khac:',khac)  