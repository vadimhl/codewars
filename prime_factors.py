# https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python

def prime_factors1(n):
    pf = {}
    p = list(range(2, n//2))[::-1]
    while p:
        pr = p[-1]
        if pr == 0 :
            p.pop()
            continue
        while n % pr == 0:
            pf[pr] = pf.get(pr, 0) + 1
            n //= pr
        if n == 1:
            break
        p[::-pr] = [0] * len(p[::-pr])

    return ''.join( f'({x}' + (f'**{p})' if p > 1 else ')') for x, p in pf.items())

def prime_factors(n):
    pf = {}
    p = list(range(2, int(n**0.5)))
    for i in range(len(p)):
        pr = p[i]
        if pr == 0 :
            continue
        while n % pr == 0:
            pf[pr] = pf.get(pr, 0) + 1
            n //= pr
        if n == 1:
            break
        k = i
        while k < len(p):
            p[k] = 0
            k += pr
    if n != 1:
        pf[n] = pf.get(n, 0) + 1
    return ''.join( f'({x}' + (f'**{p})' if p > 1 else ')') for x, p in pf.items())
print(prime_factors(86240))