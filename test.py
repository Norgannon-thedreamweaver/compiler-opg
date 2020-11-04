import sys,re

VN=['E','T','F']
VT=['+','*','(',')','i']

dic = {"+": 0, "*": 1, "i": 2, "(": 3, ")": 4, "#": 5}
mat = [[1,-1,-1,-1,1,1],[1,1,-1,-1,1,1],[1,1,-2,-2,1,1],[-1,-1,-1,-1,0,-2],[1,1,-2,-2,1,1],[-1,-1,-1,-1,-2,-2]]
stack=[]

input = sys.argv[1]
line = open(input,'r').readline()
string = "#"+line.strip()+"#"
strin=list(string)
read_char=strin.pop(0)
stack.append(read_char)
read_char=strin.pop(0)
while True:
    if stack[-1] in VN:
        a=stack[-2]
    else:
        a=stack[-1]
    if a=='#' and read_char=='#':
        break

    if mat[dic[a]][dic[read_char]]==-1:
        stack.append(read_char)
        print('I'+read_char)
        read_char=strin.pop(0)
        
    elif mat[dic[a]][dic[read_char]]==1:
        if a=='+' or a=='*':
            if stack[-1]=='E' and (stack[-2]=='+' or stack[-2]=='*') and stack[-3]=='E':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('E')
                print('R')
            else:
                print('RE')
                break
        elif a==')':
            if stack[-1]==')' and stack[-2]=='E' and stack[-3]=='(':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('E')
                print('R')
            else:
                print('RE')
                break
        else:
            stack.pop()
            stack.append('E')
            print('R')
    elif mat[dic[a]][dic[read_char]]==0:
        stack.append(read_char)
        print('I'+read_char)
        read_char=strin.pop(0)
        
    else:
        print('E')
        break

