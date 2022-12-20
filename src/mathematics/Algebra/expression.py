from ..Base.base import base, _arithmetic
from ..Base.rules import rule

class expression(base, _arithmetic):
    pass

@rule
def assosiative_property(self):
    if not hasattr(self, '__iter__'):
        return self
    selftype: type = type(self)
    new = []
    for term in self:
        if type(term) == selftype:
            new.extend(term)
            continue
        new.append(term)
    if new == tuple(self):
        return self
    return selftype(new)

@rule
def commutative_property(self):
    return self

 
@rule
def distribute(self):
    return NotImplemented

@rule
def combine(self):
    if not hasattr(self, 'superoper'):
        return self
    superoper = self.superoper
    for term in self:
        pass
    return NotImplemented
class commutative(expression, tuple):
    pass

class nonCommutative(expression):
    pass
