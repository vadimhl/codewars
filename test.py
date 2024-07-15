# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python
def row_sum_odd_numbers(n):
    st = 1
    for n in range(1,5):
        print(f'{n=}  {2*n*(2*(n-1))//2}')
print(row_sum_odd_numbers("3"))
# 0 2 4 6   8  10
#   2 6 12 20  30
'''
                     1
                  3     5
               7     9    11
           13    15    17    19
        21    23    25    27    29
    31


'''