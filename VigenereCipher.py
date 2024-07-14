def solution(lst):
    n = min(lst) 
    s = set(lst)
    while any( x % n for x in lst ):
        mx = max(s) 
        s.remove(mx)
        n = mx - max(s)
        s.add(n)
    return n * len(lst)

print(solution ([3, 13, 23, 7, 83]))