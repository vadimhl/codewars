# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python

def choose_best_sum1(t, k, ls):
    d = [[-1] * (len(ls)+1) for _ in range(t + 1)]
    def rec(l, n):
        if l == 0 or n == 0:
            return 0
        if d[l][n] != -1:
            return d[l][n]
        if ls[n - 1] <= l:
            d[l][n] = max(ls[n - 1] + rec(l - ls[n - 1], n - 1),  rec(l, n - 1))
        else:
             d[l][n] = rec(l, n - 1)
        return d[l][n]
    return rec(t, len(ls))

def choose_best_sum(t, k, ls):
    n = len(ls)
    d = [ [-1] * (n+1) for _ in range(t + 1)]
    def rec(t, i):
        if i == 0 or t <= 0:
            return 0
        if d[t][i] != -1:
            return d[t][i]
        if i == k:
            s = sum(ls[:n])
            d[t][i] = s if s < t else None
        return rec(t - ls[i], i - 1)
        

    return rec(t, n-1)
ts = [50, 55, 56, 57, 58]
ts = [50]

print(choose_best_sum(163, 3, ts)) 
163