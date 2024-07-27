# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/python
class Number:
    def __init__(self, num) -> None:
        self.num = num
    def val(self, args = None):
        if not args:
            return self.num
        else:
            return args(self.num)

zero = Number(0).val
one = Number(1).val
two = Number(2).val
three = Number(3).val
four = Number(4).val
five = Number(5).val
six = Number(6).val
seven = Number(7).val
eight = Number(8).val
nine = Number(9).val

def plus(op): 
    return (lambda a: a + op)
def minus(op): 
    return (lambda a: a - op)
def times(op):
    return (lambda a: a * op)
def divided_by(op):
    return (lambda a: a // op)
print(six(divided_by(two())))