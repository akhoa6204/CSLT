def token(s):
    s = s.replace(' ', '')
    tokens = []
    i = 0

    while len(s) > i:
        if s[i] == '*' or s[i] == '/' or s[i] == '^' or s[i] == '(' or s[i] == ')':
            tokens.append(s[i])
            i += 1
        elif s[i] == '+' or s[i] == '-':
            if i > 0 and ('9' <= s[i-1] >= '0' or s[i-1] == ')'):
                tokens.append(s[i])
                i += 1
            else:
                num = s[i]
                i += 1

                while len(s) > 1 and '9' <= s[i] >= '0':
                    num += s[i]
                    i += 1
                tokens.append(num)
        elif '9' <= s[i] >= '0':
            num = ''
            
            while len(s) > 1 and '9' <= s[i] >= '0':
                num += s[i]
                i += 1
                tokens.append(num)
        else:
            return []
    return tokens

def main():
    s = input('Enter a mathematical expression: ')
    print('The tokens are: {}'. format(token(s)))

if __name__ == '__main__':
    main()
