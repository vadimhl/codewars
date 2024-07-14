# https://www.codewars.com/kata/5571d9fc11526780a000011a/train/python
class Is_the:
    def __init__(self, thing):
        self.thing = thing
    def __getattr__(self, item):
        print(item)
        return self.thing
        
class Is_a:
    def __init__(self, thing):
        self.thing = thing
    def __getattr__(self, item):
        setattr(self.thing, 'is_a_' + item, True)
        return self.thing

class Is_not_a:
        def __init__(self, thing):
            self.thing = thing
        def __getattr__(self, item):
            setattr(self.thing, 'is_a_' + item, False)
            return self.thing        

class SetAtr:
    def __init__(self, thing, attr = None):
        self.thing = thing
        self.attr = attr
    def __getattr__(self, item):
        if self.attr:
            setattr(self.thing, self.attr, item)
            return self.thing
        return SetAtr(self.thing, item)
    
class Has:
    def __init__(self, thing, cnt):
          self.thing = thing
          self.cnt = cnt
    def __getattr__(self, item):
        if self.cnt > 1:
            setattr(self.thing, item, Thing(item, [Thing('')]*self.cnt))
            return getattr(self.thing, item)
        elif self.cnt > 1:
            setattr(self.thing, item, Thing(item))
            return getattr(self.thing, item)



class Thing:
    def __init__(self, name, seq = []):
        self.name = name
        self.is_a = Is_a(self)
        self.is_not_a = Is_not_a(self)
        self.is_the = Is_the(self)
        self.seq = seq
    
    def __iter__(self):
        return self.seq
    def __getitem__(self, n):
        return self.seq[n]
    def __len__(self):
        return len(self.seq)
    
    def has(self, cnt):
         return Has(self, cnt)
    
    def __getattr__(self, item):
        print(item)
        if item == 'is_the':
             return SetAtr(self)
            
jane = Thing('Jane')



#jane.is_a.person
#jane.is_the.parent_of.joe
legs = jane.has(2).legs
print(len(legs)) # => 2
print(isinstance(legs, Thing)) # => True
print(isinstance(jane.legs[0], Thing) )