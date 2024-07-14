# https://www.codewars.com/kata/5993c1d917bc97d05d000068/train/python
def regex_divisible_by(n):
    r = [2 % n]
    for i in range(1, n * 2):
        r.append( (2 * r[-1]) % n)
    if not 0 in r:
        minr = min(r)
        st = r.index(1)
        # print (f'{m=}  {r}  {st=} {r[st+1:]}')    
        r1 = r[st: st + 1 + r[st+1:].index(1)]
        print (f'{n=} {r}  {r1}')    
        re = ''.join([ '1' if x in r1 else '+' for x in range(max(r1) + 1)])
        print( re)
    else:
        print(f' {r}  ')

regex_divisible_by(7)        