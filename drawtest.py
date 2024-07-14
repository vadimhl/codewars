from tkinter import *
def draw_path(path, crs, stations, a_train, a_pos, b_train, b_pos, a_stop, b_stop,  it):
    print(f' drw {a_pos=} {a_stop=}')
    print(f' drw {b_pos=} {b_stop=}')

    def click(event):
        grid_position = [event.x, event.y]
        print(grid_position)
        it()

    def cell(x, y, d = 0, color = None) :
        xs, ys = x * scale + 2 - d, y * scale + 2 - d
        xs1, ys1 = x * scale + scale - 2 + d, y * scale + scale -2 + d
        canvas.create_line(xs, ys, xs1, ys,fill=color)
        canvas.create_line(xs1, ys, xs1, ys1,fill=color)
        canvas.create_line(xs1, ys1, xs, ys1, fill=color)
        canvas.create_line(xs, ys1, xs, ys, fill=color)

    window = Tk()
    window.title('Test')
    canvas = Canvas(window, width=1600, height=800 )
    canvas.pack()

    scale = 60
    # adir = 1 if a_train[0] == 'a' else -1
    # bdir = 1 if b_train[0] == 'b' else -1
    # a_f = min(a_pos, a_pos + (len(a_train) -1) * adir)
    # a_l = max(a_pos, a_pos + (len(a_train) -1) * adir)
    # b_f = min(b_pos, b_pos + (len(b_train) -1) * bdir)
    # b_l = max(b_pos, b_pos + (len(b_train) -1) * bdir)
    for x, y in stations:
            cell(x, y, 1, 'blue')
    for x, y, symb, dir, pos in path:
        cell(x, y)

        canvas.create_text(x * scale+15, y * scale+15, text=f'{x}:{y}', fill="black", font=('Helvetica 12'))
        if (x,y) in crs:
            nc = crs[(x,y)].index(pos)
            canvas.create_text(x * scale+45, y * scale+15+ 15*nc, text=str(pos), fill="black", font=('Helvetica 12'))
        else:
            canvas.create_text(x * scale+45, y * scale+15, text=str(pos), fill="black", font=('Helvetica 12'))
        if pos in a_train: #a_f <= pos <= a_l:
            canvas.create_text(x * scale+15, y * scale+30, text=f'a', fill="red", font=('Helvetica 12'))
        if pos in b_train: #b_f <= pos <= b_l:
            canvas.create_text(x * scale+15, y * scale+30, text=f'b', fill="green", font=('Helvetica 12'))

    window.bind('<Button-1>', click)

    window.mainloop()



