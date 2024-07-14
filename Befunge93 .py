# https://www.codewars.com/kata/526c7b931666d07889000a3c/train/python
import random

def interpret(code):
    output = ""
    stack = []

    code = code.splitlines()
    line, pos = 0, 0
    dr = 'r'

    def pop():
        if stack:
            return stack.pop()
        else:
            return 0

    def push(x):
        stack.append(x)
    
    stringMode = False
    Trampoline = False
    cnt = 50000
    while True and (cnt := cnt - 1):
        print(f'{dr=} {line=} {pos=} {cnt=}')        
        cmd = code[line][pos]
        print(f'{cmd=} ')
        if stringMode:
            if cmd == '"':
                stringMode = False
            else:
                push(ord(cmd))
        elif Trampoline:
            Trampoline = False
        else:
            match cmd:
                case '0':
                    push(int(cmd))
                case '1':
                    push(int(cmd))
                case '2':
                    push(int(cmd))
                case '3':
                    push(int(cmd))
                case '4':
                    push(int(cmd))
                case '5':
                    push(int(cmd))
                case '6':
                    push(int(cmd))
                case '7':
                    push(int(cmd))
                case '8':
                    push(int(cmd))
                case '9':
                    push(int(cmd))

                case '+':
                    push(pop()+pop())
                case '-':
                    a = pop()
                    b = pop()
                    push(b -a)
                case '*':
                    push(pop()*pop())
                case '/':
                    a = pop()
                    b = pop()
                    push(b / a if a else 0)
                case '%':
                    a = pop()
                    b = pop()
                    push(b % a if a else 0)
                case '!':
                    push(int(not pop()))
                case '`':
                    a = pop()
                    b = pop()
                    push(int(b>a))
                case '>':
                    dr = 'r'
                case '<':
                    dr = 'l'
                case '^':
                    dr = 'u'
                case 'v':
                    dr = 'd'
                case '?':
                    dr  = random.choice('lrud')
                case '_':
                    if pop():
                        dr = 'l'
                    else:
                        dr = 'r'
                case '|':
                    if pop():
                        dr = 'u'
                    else:
                        dr = 'd'
                case '"':
                    stringMode = True
                case ':':
                    a = pop()
                    push(a)
                    push(a)
                case '\\': 
                    a = pop()
                    b = pop()
                    push(a)
                    push(b)
                case '$': 
                    pop()
                case '.':
                    output += str(pop())
                case ',':
                    output += chr(pop())
                case '#':
                    Trampoline = True
                case 'p':
                    y = pop()
                    x = pop()
                    v = pop()
                    code[y] = code[y][:x] + chr(v) + code[y][x + 1:] 
                case 'g':
                    y = pop()
                    x = pop()
                    print(f'{x=} {y=}')
                    push(ord(code[y][x]))
                case '@':
                    break

        print(f'{stack=}')        
        print(f'{output=}')        

        match dr:
            case 'r':
                pos += 1
                if pos >= len(code[line]):
                    pos = 0
                    line += 1
            case 'l':
                pos -= 1
                if pos < 0:
                    pos = 0
                    line -= 1
            case 'd':
                line += 1
            case 'u':
                line -= 1



    return output

code = '>987v>.v\nv456<  :\n>321 ^ _@'
code='>25*"!dlroW olleH":v\n                v:,_@\n                >  ^'
code='2>:3g" "-!v\\  g30          <\n |!`"&":+1_:.:03p>03g+:"&"`|\n @               ^  p3\\" ":<\n2 2345678901234567890123456789012345678' 
res = interpret(code)
print(res)
# > 9 8 7 v >.v
# v 4 5 6 <   :
# > 3 2 1  ^_ @
#     0    1    2    3    4    5    6    7    8    9    0    1    2    3    4    5    6    7    8    9 
# 0 ['2', '>', ':', '3', 'g', '"', ' ', '"', '-', '!', 'v', '\\', ' ', ' ', 'g', '3', '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '<']
# 1 [' ', '|', '!', '`', '"', '&', '"', ':', '+', '1', '_', ':', '.', ':', '0', '3', 'p', '>', '0', '3', 'g', '+', ':', '"', '&', '"', '`', '|']
# 2 [' ', '@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '^', ' ', ' ', 'p', '3', '\\', '"', ' ', '"', ':', '<']
# 3 ['2', ' ', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8']



# 0 ['>', '2', '5', '*', '"', '!', 'd', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'l', 'e', 'H', '"', ':', 'v']
# 1 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'v', ':', ',', '_', '@']
# 2 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '>', ' ', ' ', '^']
