# https://www.codewars.com/kata/53005a7b26d12be55c000243/train/python

import re

# def lastp(li:list[str]):
#     return next(i for i in reversed(range(len(li))) if li[i] == ')')


def tokenize(expression):
    if expression == "":
         return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]

class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}
        operators = {'+', '-', '*', '/', '%'}

    def tree(self):
        stack, i = [], 0
        while i < len(self.tokens):
            if self.tokens[i] == '(':
                stack.append(i)
            elif self.tokens[i] == ')':
                j = stack.pop()
                self.tokens[j: i + 1] = [self.prior(self.tokens[j + 1: i])]
                i = j 
            i += 1

    def prior(self, tokens):
        operators = [['='], ['+', '-'], ['*', '/', '%']]
        for ops in operators:
            if i := next((x for x in range(len(tokens))[::-1] if tokens[x] in ops), None):
                return [self.prior(tokens[:i]), Node(tokens[i]),  self.prior(tokens[i+1:])]
        if len(tokens) != 1:
            raise ValueError('Bad expr')
        return Node(tokens[0], self) if isinstance(tokens[0], str) else tokens[0]

    def calc(self, tokens):
        if isinstance(tokens, list):
            if tokens[1].dat == '=':
                a2 = self.calc(tokens[2])
                self.vars[tokens[0].dat] = a2
                print(f'calc {self.vars=}')
                return a2
            a1 = self.calc(tokens[0])
            a2 = self.calc(tokens[2])
            match tokens[1].dat:
                case '+' : return a1 + a2
                case '-' : return a1 - a2
                case '*' : return a1 * a2
                case '/' : return a1 / a2
                case '%' : return a1 % a2
        else:
            return tokens.calc()

    def input(self, expression):
        self.tokens = tokenize(expression)
        self.tree()    
        self.tokens = self.prior(self.tokens)
        print(f'{self.tokens=}')
        
        res = []
        print(prtree(self.tokens))
        return self.calc(self.tokens)

class Node:
    def calc(self):
        return self.dat if self.type == 'const' else self.vars[self.dat]
    def __repr__(self) -> str:
        return f'{self.type}: {self.dat}'
    def __str__(self) -> str:
        return f'{self.type}: {self.dat}'
    def __init__(self, token:str, interpreter: Interpreter = None) -> None:
        if interpreter:
            self.vars = interpreter.vars
        if token in {'+', '-', '*', '/', '%', '='}:
            self.type = 'oper'
            self.dat = token
        elif token.isidentifier():
            self.type = 'var'
            self.dat = token
        elif token.isdigit():
            self.type = 'const'
            self.dat = int(token)
        elif token.isdigit():
            self.type = 'const'
            self.dat = int(token)                        
        else:
            self.type = 'const'
            self.dat = float(token)

def prtree(tokens, last = True, header = ''):
    elbow = "└──"
    pipe = "│  "
    tee = "├──"
    blank = "   "
    if isinstance(tokens, list):
        ret = header + (elbow if last else tee)+ str(tokens[1]) +'\n'
        ret += prtree(tokens[0], False, header + (blank if last else pipe)) 
        ret += prtree(tokens[2], True, header + (blank if last else pipe)) 
        return ret
    else:
        return header + (elbow if last else tee) + str(tokens)+'\n'

interpreter = Interpreter()
expr = "( 3 + 2.5 )* (8 - 6)"
expr = '1 2'
print(interpreter.input(
    expr
    ))

'''
expression      ::= factor | expression operator expression
factor          ::= number | identifier | assignment | '(' expression ')'
assignment      ::= identifier '=' expression

operator        ::= '+' | '-' | '*' | '/' | '%'

identifier      ::= letter | '_' { identifier-char }
identifier-char ::= '_' | letter | digit

number          ::= { digit } [ '.' digit { digit } ]

letter          ::= 'a' | 'b' | ... | 'y' | 'z' | 'A' | 'B' | ... | 'Y' | 'Z'
digit           ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'




'''
