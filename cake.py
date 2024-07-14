# https://www.codewars.com/kata/586214e1ef065414220000a8/train/python

def cut(cakestr:str):
    def rinp(xpos, ypos, shape):
        cnt = 0
        for x in range(xpos, xpos + shape[0]):
            for y in range(ypos, ypos + shape[1]):
                # print(f'{x=} {y=} {cake[y][x]=} {cnt=}')
                if cake[y][x] == 'o':
                    cnt += 1
        return cnt

    def fill(xpos, ypos, shape):
        for x in range(xpos, xpos + shape[0]):
            for y in range(ypos, ypos + shape[1]):
                # print(f'{x=} {y=} {tc[y][x]=} ')
                tc[y][x] = 1

    def unfill(xpos, ypos, shape):
        for x in range(xpos, xpos + shape[0]):
            for y in range(ypos, ypos + shape[1]):
                # print(f'{x=} {y=} {tc[y][x]=} ')
                tc[y][x] = 0


    def isempty(xpos, ypos, shape):
        for x in range(xpos, xpos + shape[0]):
            for y in range(ypos, ypos + shape[1]):
                # print(f'{x=} {y=} {tc[y][x]=} ')
                if tc[y][x] : return False
        return True

    def findempt():
        nonlocal filled
        for x in range(0, ncols):
            for y in range(0, nrows):
                # print(f'{x=} {y=} {tc[y][x]=} ')
                if tc[y][x] == 0 : return x, y
        print('Filled??????')
        filled = True
        return None, None

    def putshape():
        x, y = findempt()
        print(f'{x=} {y=} {filled=}')
        if filled :return True
        for shape in shapes:
            if x + shape[0] <= ncols and y + shape[1] <= nrows:
                if rinp(x, y, shape) == 1 and isempty(x, y, shape):
                    fill(x, y, shape)
                    r = putshape()
                    if r:
                        result.append((x, y, shape))
                        return True
                    else:
                        unfill(x, y, shape)

    def piece(p):
        xpos, ypos, shape = p
        
        res = ''
        for y in range(ypos, ypos + shape[1]):
            # print(f'{xpos=} {ypos=} {y=} {shape=} ')
            res += cake[y][xpos: xpos +shape[0]] + '\n'
        return res.strip()

    nr = cakestr.count('o')
    cake = cakestr.splitlines()
    nrows = len(cake)
    ncols = len(cake[0])
    raisins = []
    if nrows * ncols % nr:
        return []
    size = nrows * ncols // nr
    shapes = []
    for i in range(ncols, 0, -1 ):
        if size % i == 0 and size // i <= nrows:
            shapes.append((i, size // i))

    for y, row in enumerate(cake):
        for x, c in enumerate(row):
            if c == 'o':
                raisins.append((x, y))

    print(f'{nr = } {size=} {nrows = } {ncols = } {raisins=}')
    print(f'{shapes = }')
    tc = [ [0] * ncols for _ in range(nrows)]
    filled = False
    for row in tc:
        print(' '.join(map(str,row)))
    result = [] 
    putshape() 
    result.sort(key = lambda x: x[1]*ncols + x[0] )   
    print(f'{result=}')  
    return list(map(piece, result))

cake = '''
........
..o.....
...o....
........
'''.strip()
cake = '''
.o.o....
........
....o...
........
.....o..
........
'''.strip()

print(cut(cake))