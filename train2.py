from drawtest import draw_path 

class Train:
    def __str__(self) -> str:
        return f' {self.pos =} {self.dir =}  {self.stop =}  {self.cells =}'
    def settrain(self):
        self.cells = set()
        for p in range(self.pos, self.pos + self.len * self.dir, self.dir):
            self.cells.add( p % self.lenp)

    def __init__(self, train_str, st_pos, lenp) -> None:
        self.dir = 1 if train_str[0] == 'a' else -1
        self.len = len(train_str)
        self.lenp = lenp
        self.pos = st_pos
        self.stop = 0
        self.settrain()

def train_crash(track, a_train, a_pos, b_train, b_pos, limit):
    print(f'{track =}')
    print(f'{a_train =}')
    print(f'{a_pos =}')
    print(f'{b_train =}')
    print(f'{b_pos =}')
    print(f'{limit=}')

    def it():
        print(f' it {a_pos=} {a_stop=}')
        print(f' it {b_pos=} {b_stop=}')

        for st in stations:
            if not a_stop and st == a_pos:
                a_stop = a_len 
                print(f'   A station {i=} {st=} {a_pos=} {a_stop=}')

            if not b_stop and st == b_pos:
                b_stop = b_len + 1
                print(f'   B station {i=} {st=} {b_pos=} {b_stop=}')

        if a_stop:
            a_stop -= 1
        if not a_stop:
            a_pos = (a_pos + adir) % lenp
            # a_train = settrain(a_pos, a_len, adir)

        if b_stop:
            b_stop -= 1
        if not b_stop:
            b_pos = (b_pos + bdir) % lenp
            # b_train = settrain(b_pos, b_len, bdir)

        if pos_in_train(b_pos, a_pos, a_len ) or pos_in_train( b_pos + b_len, a_pos, a_len ):
            return i
        for c in crs.values():
            if (( c[0] in a_train  or c[1] in a_train ) and 
                (c[0] in b_train or c[1] in b_train )):
                return i                


    def pos_in_train(pos, train_pos, train_len):
        return train_pos <= pos <= train_pos + train_len


    def move(pos, dir):
        mv = {'r': (1, 0), 'l': (-1, 0), 'd': (0, 1), 'u': (0, -1), 'rd': (1, 1), 'ru': (1, -1), 'ld': (-1, 1), 'lu': (-1, -1)}
        return (pos[0] + mv[dir][0], pos[1] + mv[dir][1])
    
    def gsymb(pos):
        # print(f'      gs  {pos=} {len(tr)=} {len(tr[pos[1]])=}')
        if 0 <= pos[1] < len(tr):
            if 0 <= pos[0] < len(tr[pos[1]]):
                return tr[pos[1]][pos[0]]
        return ' '
    
    def new_dir(symb, dir):
        if symb == '\\':
            if dir in ('r', 'rd', 'd'):
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
    
    crs, stations = {}, {}
    adir = 1 if a_train[0] == 'a' else -1
    bdir = 1 if b_train[0] == 'b' else -1
    a_len = len(a_train)
    b_len = len(b_train)

    tr = track.splitlines()
    # for line in tr:
    #     print(line)
    st = (tr[0].index('/'),0)
    dir = 'r'
    lenp = 0
    pos = st
    symb = gsymb(pos)
    path = [(pos[0], pos[1], symb, dir, lenp)]    

    while (pos := move(pos, dir)) != st :
        lenp  += 1
        try:
            symb = gsymb(pos)
            path.append((pos[0], pos[1], symb, dir, lenp))
            dir = new_dir(symb, dir)
        except:
            for line in tr:
                print('s'+line+'e')
            print(f'Err! {pos=} {dir=} {symb=}')
            return

        if symb in '+x': 
            crs[pos] = crs.get(pos, []) + [lenp]
        if symb == 'S':
            stations[pos] = stations.get(pos, []) + [lenp]
    for i, v in stations.items():
        if len(v) > 1:
            crs[i] = crs.get(i, []) + v
    print(Train(a_train, a_pos, lenp))
    return
    print(f'{crs=} ')
    print(f'{stations=}')
    a_train = settrain(a_pos, a_len, adir)
    b_train = settrain(b_pos, b_len, bdir)
    print(f'{a_train}')
    lenp += 1
    a_stop, b_stop = 0, 0
    print(f' {a_pos=} {a_stop=}')
    print(f' {b_pos=} {b_stop=}')

    draw_path(path, crs, stations, a_train, a_pos, b_train, b_pos, a_stop, b_stop, it)
    
    # for i in range(limit):
    #     it()
    # return -1      

track ='/-------\\ \n|       | \n|       | \n|       | \n\\-------S--------\\\n        |        |\n        S        |\n        |        |\n        \\--------/\n\n'
a_train ='aaaaaA'
a_train_pos =15
b_train ='bbbbbB'
b_train_pos =5
limit=10
print(train_crash(track, a_train, a_train_pos, b_train, b_train_pos, limit))
