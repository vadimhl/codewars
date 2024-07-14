import re
n = 2
for  m in range(1, 10):
    r = [n % m]
    for i in range(1, m * 2):
        r.append( (2 * r[-1]) % m)
    if not 0 in r:
        minr = min(r)
        st = r.index(minr)
        print (f'{m=}  {r}  {st=} {r[st+1:]}')    
        r1 = r[st: st + 1 + r[st+1:].index(minr)]
        re = ''.join([ '1' if x in r1 else '+' for x in range(max(r1) + 1)][::-1])
        print (f'{m=}  {r}  {r1} {re}')    
        
    else:
        print(f'{m=}  {r}  ')
'''
2  1    4   2   1   4    2   
6  5    4   3   2   1    0
                1   1    1  
            1   1   1    0
        1   0   1   0    1
        1   1   1   0    0
   1    0   0   0   1    1
   1    0   1   0   1    0
   1    1   0   0   0    1
   1    1   1   0   0    0
   1    1   1   1   1    1
1  0    0   0   1   1    0

4  2  1  3  4  2
         1  0  1
      1  0  1  0
      1  1  1  1
   1  0  1  0  0
   1  1  0  0  1
   1  1  1  1  0
1  0  0  0  1  1
1  0  1  0  0  0
1  0  1  1  0  1
1  1  0  0  1  0


'''