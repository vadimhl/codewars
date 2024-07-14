# https://www.codewars.com/kata/59b47ff18bcb77a4d1000076/train/python
def train_crash(track, a_train, a_train_pos, b_train, b_train_pos, limit):
    print(f'{track =}')
    print(f'{a_train =}')
    print(f'{a_train_pos =}')
    print(f'{b_train =}')
    print(f'{b_train_pos =}')
    print(f'{limit=}')

    def pos_in_train(pos, train_pos, train_len):
        return train_pos <= pos <= train_pos + train_len


    def move(pos, dir):
        mv = {'r': (1, 0), 'l': (-1, 0), 'd': (0, 1), 'u': (0, -1), 'rd': (1, 1), 'ru': (1, -1), 'ld': (-1, 1), 'lu': (-1, -1)}
        return (pos[0] + mv[dir][0], pos[1] + mv[dir][1])
    
    def gsymb(pos):
        # print(f'      gs  {pos=} {len(tr)=} {len(tr[pos[1]])=}')
        return tr[pos[1]][pos[0]]
    
    def new_dir(symb, dir):
        if symb == '\\':
            if dir in ('r', 'rd', 'd'):
                # print(f'    nd  {pos=} {symb=} {dir=}')
                if gsymb(move(pos,'rd')) != ' ':
                    return 'rd'
                elif gsymb(move(pos,'r')) != ' ':
                    return 'r'
                else:
                    return 'd'
            else:
                if gsymb(move(pos,'lu')) != ' ':
                    return 'lu'
                elif gsymb(move(pos,'l')) != ' ':
                    return 'l'
                else:
                    return 'u'
        if symb == '/':
            if dir in ('u', 'ru', 'r'):
                if gsymb(move(pos,'ru')) != ' ':
                    return 'ru'
                elif gsymb(move(pos,'r')) != ' ':
                    return 'r'
                else:
                    return 'u'
            else:
                if gsymb(move(pos,'ld')) != ' ':
                    return 'ld'
                elif gsymb(move(pos,'d')) != ' ':
                    return 'd'
                else:
                    return 'l'
        return dir
    
    crs, stations = {}, set()
    adir = 1 if a_train[0] == 'a' else -1
    bdir = 1 if b_train[0] == 'b' else -1
    a_len = len(a_train)
    b_len = len(b_train)

    tr = track.splitlines()
    maxl = len(max(tr, key=len))
    # print(f'{maxl}')
    tr = [ [' '] + list(line) + [' '] * (maxl - len(line) + 1)   for line in tr]
    maxl += 2
    tr = [[' '] * maxl] + tr + [[' '] * maxl]
    # for line in tr:
    #     print(''.join(line))
    st = (tr[1].index('/'), 1)
    dir = 'r'
    lenp = 0
    pos = st
    #pos  = move(st, dir)
    symb = gsymb(pos)
    path = [(pos[0], pos[1], symb, dir, lenp)]

        # if lenp in atrain:
        #     tr[pos[1]][pos[0]] = 'a'
        # if lenp in btrain:
        #     tr[pos[1]][pos[0]] = 'b'

        #pos  = move(pos, dir)

        
    for line in tr:
        print(''.join(line))

    lenp += 1
    # print(f'{pos=} {lenp=} ')
    print(f'{len(path)} {lenp=} ')
    print(f'{crs=} ')
    print(f'{path=}')
    print(f'{stations=}')
    a_stop, b_stop = 0, 0
    for i in range(limit):
        print(f'{i=} {a_train_pos=} {a_stop=}')
        print(f'    {b_train_pos=} {b_stop=}')
        for st in stations:
            if not a_stop and st == a_train_pos:
                a_stop = a_len 
                print(f'   A station {i=} {st=} {a_train_pos=} {a_stop=}')

            if not b_stop and st == b_train_pos:
                b_stop = b_len + 1
                print(f'   B station {i=} {st=} {b_train_pos=} {b_stop=}')

        if a_stop:
            a_stop -= 1
        if not a_stop:
            a_train_pos = (a_train_pos + adir) % lenp

        if b_stop:
            b_stop -= 1
        if not b_stop:
            b_train_pos = (b_train_pos + bdir) % lenp

        if pos_in_train(b_train_pos, a_train_pos, a_len ) or pos_in_train( b_train_pos + b_len, a_train_pos, a_len ):
            return i
        for c in crs.values():
            if ((pos_in_train(c[0], a_train_pos, a_len ) or pos_in_train(c[1], a_train_pos, a_len ) ) and 
                (pos_in_train(c[0], b_train_pos, b_len ) or pos_in_train(c[1], b_train_pos, b_len ) ) ):
                return i                


    return -1      
        
track ='/-------\\ \n|       | \n|       | \n|       | \n\\-------+--------\\\n        |        |\n        S        |\n        |        |\n        \\--------/\n\n'
a_train ='aaaaaA'
a_train_pos =15
b_train ='bbbbbB'
b_train_pos =5
limit=10
# print(train_crash(TRACK_EX, "Aaaa", 147, "Bbbbbbbbbbb", 288, 1102))
print(train_crash(track, a_train, a_train_pos, b_train, b_train_pos, limit))
'''                cw         acw
r  = ( 1,  0) : ( 1,  1)   ( 1, -1)
rd = ( 1,  1) : ( 0,  1)   ( 1,  0)
d  = ( 0,  1) : (-1,  1)   ( 1,  1)
ld = (-1,  1) : (-1,  0)   ( 0,  1)
l  = (-1,  0) : (-1, -1)   (-1,  1)
lu = (-1, -1) : ( 0, -1)   (-1,  0)
u  = ( 0, -1) : ( 1, -1)   (-1, -1)
ru = ( 1, -1) : ( 1,  0)   ( 0, -1)


# r  - \  rd, d
# rd \ \  rd, d
# d  | \  rd, d
# 
# l  - \  lu, u
# lu \ \  lu, u
# u  | \  lu, u   


        #u  | /  ru, u
        #ru / /  ru, u
        #r  - /  ru, u
        #
        #d  | /  ld, l
        #ld / /  ld, l
        #l  - /  ld, l



r  (1, 0) \  rd, d
rd (1, 1) \  rd, d
d  (0, 1) \  rd, r

l  (-1, 0)  \  lu, u
lu (-1, -1) \  lu, u
u  (0, -1)  \  lu, u   


u  (0, -1) /  ru, u
ru (1, -1) /  ru, u
r  (1, 0)  /  ru, u

d  ( 0, 1) /  ld, l
ld (-1, 1) /  ld, l
l  (-1, 0) /  ld, l


 
d  (0, 1) 
l  (-1, 0) 
lu (-1, -1)
 

mv = {r: (1, 0), l: (-1, 0), d: (0, 1), u: (0, -1), rd: (1, 1), ru: (1, -1), ld: (-1, 1), lu: (-1, -1)}



dirs = (( 1,  0),( 1,  1),( 0,  1),(-1,  1),(-1,  0),(-1, -1),( 0, -1),( 1, -1))

        if simb in '/\\':
            for ndir in dirs:
                if ndir != (-dir[0], -dir[1]):
                    if tr[pos[1] + ndir[1]][pos[0] + ndir[0]] != ' ' :
                        dir = ndir
                        break 

'''
TRACK_EX = """\
                                /------------\\
/-------------\\                /             |
|             |               /              S
|             |              /               |
|        /----+--------------+------\\        |   
\\       /     |              |      |        |     
 \\      |     \\              |      |        |                    
 |      |      \\-------------+------+--------+---\\
 |      |                    |      |        |   |
 \\------+--------------------+------/        /   |
        |                    |              /    | 
        \\------S-------------+-------------/     |
                             |                   |
/-------------\\              |                   |
|             |              |             /-----+----\\
|             |              |             |     |     \\
\\-------------+--------------+-----S-------+-----/      \\
              |              |             |             \\
              |              |             |             |
              |              \\-------------+-------------/
              |                            |               
              \\----------------------------/ 
"""