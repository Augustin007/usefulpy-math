from .expression import commutative
from ..Base.rules import rule, ruleGroup

class mul(commutative): # multiplication is only sometimes commutative, expression syntax and tree may change.
    def __new__(cls, name, *args):
        self = tuple.__new__(cls, name, args)
        self.classRules = mul.getClassRules()
        # subrules = cls

    def __str__(self, /)->str:
        return '*'.join(map(str, self)).replace('+-', '-')

    def tex(self, /)->str:
        pass

    def substitute(self, data: dict, /):
        pass

    @staticmethod
    def getClassRules()->ruleGroup:
        return ruleGroup()