# https://www.codewars.com/kata/58e24788e24ddee28e000053/train/python

def simple_assembler(program:str):
    prg = [ cmd.split(' ') + [None] for cmd in program]
    regs = {}
    val = lambda a : regs[a] if a.isalpha() else int(a)
    step = 0
    while step < len(prg):
        cmd, arg1, arg2, *_ = prg[step] 
        match cmd:
            case 'mov':
                regs[arg1] = val(arg2)
            case 'inc':
                regs[arg1] += 1
            case 'dec':
                regs[arg1] -= 1
            case 'jnz':
                if (val(arg1) ):
                    step += val(arg2)
                    continue
        step += 1
    return regs


code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''
print(simple_assembler(code.splitlines()))