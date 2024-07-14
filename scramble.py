from collections import Counter
def scramble(s1, s2):
    c1, c2 = Counter(s1), Counter(s2)
    print(all(l[1] <= c1[l[0]] for l in c2.items()))
scramble('rkqodlw', 'world')
