# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

def max_sequence(arr):
    # if not arr :return 0
    # d =[arr[-1]]
    # for x in arr[-2::-1]:
    #     d.append(max(d[-1] + x, x))
    # res = max(d)
    # return res if res > 0 else 0

    if not arr :return 0
    # d = arr[-1]
    # maxd = d
    d, maxd = 0, 0
    for x in arr[::-1]:
        d = max(d + x, x)
        maxd = max(maxd, d)
    return maxd if maxd > 0 else 0
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# , 6          2  4    3  6   2  3  1  -1  4