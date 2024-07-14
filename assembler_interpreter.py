# https://www.codewars.com/kata/58e61f3d8ff24f774400002c/train/python

import re

def assembler_interpreter(program:str):
    val = lambda a : regs[a] if a.isalpha() else int(a)
    prg, labels, regs, stack, step, cmp, msg = [], {}, {}, [], 0, 0, ''
    rgx = "(^\s*\w+\:)|(-?\w+)|('[^']*')|(;.*$)"     
    
    for row in program.splitlines():
        row = row.strip()
        if len(row) == 0:
            continue
        # print(f'{row=}')
        t = re.findall(rgx, row)
        cmd , args = '', []
        i = 0
        if t[0][0]:
            labels[t[0][0][:-1]] = len(prg) 
            i += 1
        if i < len(t) and t[i][1] and not cmd:
            cmd = t[i][1]
            i += 1
        while i < len(t) and (t[i][1] or t[i][2]):
            args.append(t[i][1] + t[i][2])
            i += 1
        # print(f'     {cmd=} {args=} {labels =}')        
        if cmd:
            prg.append((cmd, args))

        
    # for cmd in prg:
    #     print(cmd)
    # print(f'{labels=}')
    
    while step < len(prg):
        cmd, args = prg[step] 
        # print(f'{cmd=} {args=}')
        step +=1
        match cmd:
            case 'inc':
                regs[args[0]] += 1
            case 'dec':
                regs[args[0]] -= 1
            case 'mov':
                regs[args[0]] = val(args[1])
            case 'add':
                regs[args[0]] += val(args[1])                
            case 'sub':
                regs[args[0]] -= val(args[1])                
            case 'mul':
                regs[args[0]] *= val(args[1])                
            case 'div':
                regs[args[0]] //= val(args[1])                
            case 'cmp':
                cmp = regs[args[0]] - val(args[1]) # x - y               
            case 'jmp':
                step = labels[args[0]]
            case 'jne':
                if cmp:
                    step = labels[args[0]]
            case 'je':
                if not cmp:
                    step = labels[args[0]]
            case 'jge':
                if  cmp >= 0:
                    step = labels[args[0]]
            case 'jg':
                if  cmp > 0:
                    step = labels[args[0]]
            case 'jle':
                if  cmp <= 0:
                    step = labels[args[0]]
            case 'jl':
                if  cmp < 0:
                    step = labels[args[0]]
            case 'call':
                stack.append(step)
                step = labels[args[0]]
                # print(f'{stack=} {step=}')
            case 'ret':
                step = stack.pop()
            case 'end':
                return msg
            case 'msg':
                msg = ''.join([ str(val(a)) if a[0] != "'" else a.strip("'") for a in args])
    
    return 

"'(5+1)/2 = '".strip()
program='''
; My first program
mov  a, 5;comm
inc: inc  a
call function
msg  '(5+1)/2 = ', a    ; output message
end

function:
    div  a, 2
    ret
'''
print(assembler_interpreter(program))

# '(5+1)/2 = 3'

'''
; comment - comments should not be taken in consideration during the execution of the program.
msg 'Register: ', x - this instruction stores the output of the program. It may contain text strings (delimited by single quotes) and registers. The number of arguments isn't limited and will vary, depending on the program.


mov x, y - copy y (either an integer or the value of a register) into register x.
add x, y - add the content of the register x with y (either an integer or the value of a register) and stores the result in x (i.e. register[x] += y).
sub x, y - subtract y (either an integer or the value of a register) from the register x and stores the result in x (i.e. register[x] -= y).
mul x, y - same with multiply (i.e. register[x] *= y).
div x, y - same with integer division (i.e. register[x] /= y).
cmp x, y - compares x (either an integer or the value of a register) and y (either an integer or the value of a register). The result is used in the conditional jumps (jne, je, jge, jg, jle and jl)
inc x - increase the content of register x by one.
dec x - decrease the content of register x by one.

jmp lbl - jumps to the label lbl.
jne lbl - jump to the label lbl if the values of the previous cmp command were not equal.
je lbl - jump to the label lbl if the values of the previous cmp command were equal.
jge lbl - jump to the label lbl if x was greater or equal than y in the previous cmp command.
jg lbl - jump to the label lbl if x was greater than y in the previous cmp command.
jle lbl - jump to the label lbl if x was less or equal than y in the previous cmp command.
jl lbl - jump to the label lbl if x was less than y in the previous cmp command.

label: - define a label position (label = identifier + ":", an identifier being a string that does not match any other command). Jump commands and call are aimed to these labels positions in the program.
call lbl - call to the subroutine identified by lbl. When a ret is found in a subroutine, the instruction pointer should return to the instruction next to this call command.
ret - when a ret is found in a subroutine, the instruction pointer should return to the instruction that called the current function.

msg 'Register: ', x - this instruction stores the output of the program. It may contain text strings (delimited by single quotes) and registers. The number of arguments isn't limited and will vary, depending on the program.
end - this instruction indicates that the program ends correctly, so the stored output is returned (if the program terminates without this instruction it should return the default output: see below).
'''