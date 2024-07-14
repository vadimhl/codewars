def strip_comments(strng, markers):
    mark = markers[0]
    if len(markers) > 1:
        strng = strng.translate(str.maketrans(''.join(markers[1:]), mark * (len(markers)-1)))
    sl = strng.split('\n')
    res  = []
    for l in sl:
        if mark in  l:
            res.append(l[:l.index(mark)].rstrip())
        else:
            res.append(l.rstrip())

    return '\n'.join(res)

print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))