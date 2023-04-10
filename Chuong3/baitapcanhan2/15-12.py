n = int(input())
n_str = str(n)
mh = ''
for char in n_str:
    if 0>=n or n>9999:
        break
    if char == '0':
        mh += 'A'
    elif char == '1':
        mh += 'B'
    elif char == '2':
        mh += 'C'
    elif char == '3':
        mh += 'D'
    elif char == '4':
        mh += 'E'
    elif char == '5':
        mh += 'F'
    elif char == '6':
        mh += 'G'
    elif char == '7':
        mh += 'H'
    elif char == '8':
        mh += 'K'
    elif char == '9':
        mh += 'L'
print(mh)