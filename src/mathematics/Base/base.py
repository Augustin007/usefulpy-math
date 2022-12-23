'''
Base class for all CAS classes
'''

from abc import abstractmethod
import types
from . import rules


class base:
    exact: bool
    value: int
    subrules: rules.ruleGroup
    var: tuple
    fn: set
    evaluation: types.FunctionType
    system: types.FunctionType
    classRules: rules.ruleGroup

    def __repr__(self, /):
        return f'CAS[{repr(str(self))}]'
    
    @abstractmethod
    def __str__(self, /)->str:
        pass
    
    @abstractmethod
    def tex(self, /)->str:
        pass

    @abstractmethod
    def substitute(self, data: dict, /):
        pass

    def applyRules(self, /):
        test = self.subrules.apply(self)
        if test is not None:
            return test
        test = self.classRules.apply(self)
        if test is not None:
            return test
        test = self.system().globalRules.apply(self)
        if test is not None:
            return test
        return self

    def evalstr(self, /)->str:
        if self.exact:
            return str(self.value)
        return str(self)

class _arithmetic:
    def __add__(self, other):
        return add(self, other)
    
    def __radd__(self, other):
        return add(other, self)
    
    def __mul__(self, other):
        return mul(self, other)
    
    def __rmul(self, other):
        return mul(other, self)

from ..Algebra.add import add # ... etc, at the end to avoid circular import.
from ..Algebra.mul import mul