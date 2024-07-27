# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
def dig_pow(n, p):
    d = sum(int(c)**(p + i) for i, c in enumerate(str(n)))
    if d % n == 0:
        return d // n
    else :   
        return -1
print(dig_pow(46288, 3))
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51