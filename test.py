# https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python

def sort_array(source_array):
    odd = sorted((x for x in source_array if x % 2), reverse = True) 
    return [odd.pop() if x % 2 else x for x in source_array]
''.rev
'''

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  
[3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  
[1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
'''