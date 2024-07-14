# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b/train/python
import re
def expand(expr):
    a, x, b, n =re.search("\((-?\d*)?(\w)([\+\-]\d*)?\)\^(\d*)", expr).groups()
    if a == '':
        a = 1
    elif a == '-':
        a = -1
    else:
        a = int(a)
    if b:
        b = int(b)
    else:
        b = 0
    n = int(n)
    if n == 0:
        return '1'
    
    #print(f'{a=} {x=} {b=} {n=} ')
    p = []
    for _ in range(n):
        p = [1] + [p[i]+p[i+1] for i in range (0, len(p)-1)]+ [1]
    res = ''
    for k in range(n+1):
        q = p[k] * a**(n-k) * b**(k)
        s = n-k
        # print(q, s)

        if q:
            e = f'{q}{x}^{s}'
            print(e)
            if e[-2:] == '^1':
                e = e[:-2]
            if e[-3:] == f'{x}^0':
                e = e[:-3]
            if e[:2] == f'1{x}':
                e = e[1:]
            if e[:3] == f'-1{x}':
                e = '-' + e[2:]
            print(e)
            res += '+' + e
    if res[0] == '+':
        res = res[1:]
    return res.replace('+-', '-')

expr = "(x+1)^3"
print(expand(expr))

