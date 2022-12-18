'''
Base class for all CAS classes
'''

from abc import abstractmethod
import types
from . import rules


class base:
    exact: bool
    value: int
    subrules: tuple
    var: tuple
    fn: set
    evaluation: types.FunctionType
    system: types.FunctionType
    classRules: rules.rule

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
        for rule in self.subrules:
            test = rule.apply(self)
            if test:
                return test
        test = self.classRules.apply(self)
        if test:
            return test
        for rule in self.system().globalrules:
            test = rule.apply(self)
            if test:
                return test
        return self

    def evalstr(self, /)->str:
        if self.exact:
            return str(self.value)
        return str(self)

class _arithmetic:
    pass

# from ..Algebra.add import add # ... etc, at the end to avoid circular import.