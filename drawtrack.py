# https://www.codewars.com/kata/59b47ff18bcb77a4d1000076/train/python
from tkinter import *

from train import Track
from train import Train

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
def cell(x, y, d = 0, fill = 'white') :
    xs, ys = x * scale + 2 - d, y * scale + 2 - d
    xs1, ys1 = x * scale + scale - 2 + d, y * scale + scale -2 + d
    # canvas.create_line(xs, ys, xs1, ys,fill=color)
    # canvas.create_line(xs1, ys, xs1, ys1,fill=color)
    # canvas.create_line(xs1, ys1, xs, ys1, fill=color)
    # canvas.create_line(xs, ys1, xs, ys, fill=color)
    canvas.create_rectangle(xs, ys, xs1, ys1, fill=fill)

def click(event):
     global pause
     pause = not pause

def run():
    global step
    if not pause:
        for x, y, symb, dir, pos in track.path:
            fill = 'white'
            if pos in a.cells():
                fill = 'green'
            if pos in b.cells():
                fill = 'red'

            cell(x, y, 0, fill)
            # canvas.create_text(x * scale+15, y * scale+15, text=f'{x}:{y}', fill="black", font=('Helvetica 12'))
            if (x,y) in track.crs:
                nc = track.crs[(x,y)].index(pos)
                canvas.create_text(x * scale + scale//2, y * scale+ scale//4+   scale//2*nc, text=str(pos), fill="black", font=('Helvetica 8'))
            else:
                canvas.create_text(x * scale + scale//2, y * scale + 14, text=str(pos), fill="black", font=('Helvetica 10'))
        
        window.title(f'{step=}')
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
            window.after(speed, run)


track_str ='/-----------------\\\n|                 |\n|                 |\n|                 |\n|                 |\n\\---------S-------/'
a_train ='aA'
a_train_pos =10
b_train ='bbbbbB'
b_train_pos =30
limit=200
track = Track(track_str)
print(f'{track.lenp=} {len(track.path)=}')

a = Train(a_train, a_train_pos, track.lenp)
b = Train(b_train, b_train_pos, track.lenp)

window = Tk()
window.title('Test')
canvas = Canvas(window, width=1800, height=800 )
canvas.pack()

scale = 30
for x, y in track.stations:
        cell(x, y, 1, 'blue')
        cell(x, y, 2, 'blue')


pause = False
speed = 1000
window.bind('<Button-1>', click)
step = 1
window.after(speed, run)
window.mainloop()