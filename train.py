class Train:
    def __str__(self) -> str:
        return f' {self.pos= } {self.dir= }  {self.stop= }  {self.cells()= }'

    def cells(self):
        c = set()
        for p in range(self.pos, self.pos + self.len):
            c.add( p % self.lenp)
        return c

    def setstop(self):
        self.stop = self.len - 1

    def move(self, stations: dict = {}):
        # print(f'stations {self.pos=} {stations=}')
        for st in stations.values():
            if not self.stop and self.pos in st:
                self.setstop()
                # print(f'station {st}')
        if self.stop:
            self.stop -= 1
        if not self.stop:
            self.pos = (self.pos + self.dir) % self.lenp

    def __init__(self, train_str, st_pos, lenp) -> None:
        self.dir = 1 if train_str[0].islower() else -1
        self.len = len(train_str)
        self.lenp = lenp
        self.pos = st_pos
        self.stop = 0

class Track:

    _mv = {'r': (1, 0), 'l': (-1, 0), 'd': (0, 1), 'u': (0, -1), 'rd': (1, 1), 'ru': (1, -1), 'ld': (-1, 1), 'lu': (-1, -1)}
    def move(self, pos, dir):
        return (pos[0] + Track._mv[dir][0], pos[1] + Track._mv[dir][1])
    
    def gsymb(self, pos):
        # print(f'      gs  {pos=} {len(self.tr)=} {len(self.tr[pos[1]])=}')
        if 0 <= pos[1] < len(self.tr):
            if 0 <= pos[0] < len(self.tr[pos[1]]):
                return self.tr[pos[1]][pos[0]]
        return ' '
    
    def new_dir(self, pos, symb, dir):
        if symb == '\\':
            if dir in ('r', 'rd', 'd'):
                if self.gsymb(self.move(pos,'rd')) != ' ':
                    return 'rd'
                elif self.gsymb(self.move(pos,'r')) != ' ':
                    return 'r'
                else:
                    return 'd'
            else:
                if self.gsymb(self.move(pos,'lu')) != ' ':
                    return 'lu'
                elif self.gsymb(self.move(pos,'l')) != ' ':
                    return 'l'
                else:
                    return 'u'
        if symb == '/':
            if dir in ('u', 'ru', 'r'):
                if self.gsymb(self.move(pos,'ru')) != ' ':
                    return 'ru'
                elif self.gsymb(self.move(pos,'r')) != ' ':
                    return 'r'
                else:
                    return 'u'
            else:
                if self.gsymb(self.move(pos,'ld')) != ' ':
                    return 'ld'
                elif self.gsymb(self.move(pos,'d')) != ' ':
                    return 'd'
                else:
                    return 'l'
        return dir

    def __init__(self, track:str) -> None:
        self.tr = track.splitlines()
        self.st = (self.tr[0].index('/'),0)
        self.crs = {}
        self.stations = {}
        dir = 'r'
        pos = self.st
        symb = self.gsymb(pos)
        lenp = 0
        self.path = [(pos[0], pos[1], symb, dir, lenp)]
        

        while (pos := self.move(pos, dir)) != self.st :
            lenp  += 1
            try:
                symb = self.gsymb(pos)
                self.path.append((pos[0], pos[1], symb, dir, lenp))
                dir = self.new_dir(pos, symb, dir)
            except:
                for line in self.tr:
                    print('s'+line+'e')
                print(f'Err! {pos=} {dir=} {symb=}')
                return

            if symb in '+x': 
                self.crs[pos] = self.crs.get(pos, []) + [lenp]
            if symb == 'S':
                self.stations[pos] = self.stations.get(pos, []) + [lenp]
        for i, v in self.stations.items():
            if len(v) > 1:
                self.crs[i] = self.crs.get(i, []) + v
        self.lenp = lenp + 1


def train_crash(track_str, a_train, a_train_pos, b_train, b_train_pos, limit):
    print(f'{track_str =}')
    print(f'{a_train =}')
    print(f'{a_train_pos =}')
    print(f'{b_train =}')
    print(f'{b_train_pos =}')
    print(f'{limit=}')
    track = Track(track_str)
    # print(f'{track.lenp=} {len(track.path)=} {track.crs= }')
    a = Train(a_train, a_train_pos, track.lenp)
    b = Train(b_train, b_train_pos, track.lenp)
    for st in track.stations.values():
        if a.pos in st:
             a.setstop()
        if b.pos in st:
             b.setstop()

    step = 1
    while step < limit:
        ac = a.cells()
        bc = b.cells()
        print(f'{step= }  {ac= } {bc= } {a.stop=} {b.stop=} {ac & bc= }')

        if ac & bc:
            return step
        for st in track.crs.values():
            if (st[0] in ac and st[1] in bc) or (st[1] in ac and st[0] in bc):
                print(f'{step= } {st= } {ac= } {bc= } {ac & bc= }')
                return step
        else:
            step += 1
            a.move(track.stations)
            b.move(track.stations)
    return -1

track = """\
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
# a_train = "Aaaa"
# a_train_pos = 147
# b_train = "Bbbbbbbbbbb"
# b_train_pos = 288
# limit= 4000

track_str ='/-------\\ \n|       | \n|       | \n|       | \n\\-------+--------\\\n        |        |\n        S        |\n        |        |\n        \\--------/\n\n'
a_train ='aaaaaA'
a_train_pos =15
b_train ='bbbbbB'
b_train_pos =5
limit=10

track_str ='/-----------------\\\n|                 |\n|                 |\n|                 |\n|                 |\n\\-----------------/'
a_train ='aaaaaA'
a_train_pos =10
b_train ='bbbbbB'
b_train_pos =30
limit=100

track_str ='/----\\     /----\\ \n|     \\   /     | \n|      \\ /      | \n|       S       | \n|      / \\      | \n|     /   \\     | \n\\----/     \\----/'
a_train ='aaaaaA'
a_train_pos =8
b_train ='bbbbbB'
b_train_pos =20
limit=100

print(train_crash(track_str, a_train, a_train_pos, b_train, b_train_pos, limit))


