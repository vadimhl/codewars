# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python
def longest_consec(strarr, k):
    maxi, maxl= 0, 0
    lens = list(map(len, strarr))
    for i in range(k, len(strarr)+1):
        l = sum(lens[i-k:i])
        if l > maxl:
            maxi, maxl = i, l
    return ''.join(strarr[maxi-k:maxi])

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
#  "abigailtheta"