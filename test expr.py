import re

def tokenize(expression):
    if expression == "":
         return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]

vars = {}

class Oper:
    def __repr__(self) -> str:
        return f'{self.oper}'

    def __init__(self, token) -> None:
        self.oper = token
        
class Node:
    def calc(self):
        return self.dat if self.type == 'const' else self.vars[self.dat]
    def __repr__(self) -> str:
        return f'{self.dat}'
    def __init__(self, token:str, vars = None) -> None:
        self.vars = vars
        if token.isdigit():
            self.type = 'const'
            self.dat = int(token)
        if token.isidentifier():
            self.type = 'var'
            self.dat = token

def tree():
    global tokens
    stack, i = [], 0
    while i < len(tokens):
        if tokens[i] == '(':
            stack.append(i)
        elif tokens[i] == ')':
            j = stack.pop()
            tokens[j: i + 1] = [prior(tokens[j + 1: i])]
            i = j 
        i += 1

def prior(tokens):
    operators = [['='], ['+', '-'], ['*', '/', '%']]
    for ops in operators:
        if i := next((x for x in range(len(tokens))[::-1] if tokens[x] in ops), None):
            return [prior(tokens[:i]), Oper(tokens[i]),  prior(tokens[i+1:])]
    return Node(tokens[0]) if isinstance(tokens[0], str) else tokens[0]


tokens = tokenize("1+(2-3 +a) * 4 + 5")
print('st: ', tokens)
tree()
print('tr:', tokens)

print('pr:', prior(tokens))
'''
 1 2 3 3   4 4 2   5 6 6   7 7 5 1  
                                   + 
  <[<[4] + [2]>] + [<[1] * [4]>]     2> 
'''