# https://stackoverflow.com/questions/15347174/python-finding-prime-factors
# https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python
def sum_for_list(lst):
    mx = max(map(abs, lst))
    print(f"{mx=}")
    sieve = [True] * (mx + 1)
    for x in range(3, int(mx**0.5) + 1, 2):
        for y in range(3, mx // x + 1, 2):
            sieve[x*y] = False
    
    primes = [2]+[i for i in range(3,mx+1,2) if sieve[i]]
    P = {}
    print(f'{primes[-1] = }  {len(primes)=}')
    for e in lst:
        i = 0 
        while primes[i] * primes[i] < abs(e):
            if e % primes[i] == 0:
                P[primes[i]] = P.get(primes[i], 0) + e
            i += 1
            

    return sorted([[k,v] for k,v in P.items()], key=lambda a : a[0])

print(sum_for_list([575347, -62314, -91200, -644778, -463361, 759143, -65860, -255812, -654497, -135533, 703952]))