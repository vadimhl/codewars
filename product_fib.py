# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python
def product_fib(_prod):
    s1, s2 = 0, 1
    while s1 * s2 < _prod:
        s1, s2 = s2, s1 + s2
    return [s1, s2, (s1 * s2 == _prod)]



print(product_fib(4895))

'''
, [55, 89, True]

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
'''.translate()