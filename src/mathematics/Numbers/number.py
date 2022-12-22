from ..Base.base import base, _arithmetic
from ..Base.rules import rule, ruleGroup

class number:
    pass

def NumberType(name: str, rules: ruleGroup):
    type(name, (number,), general|data(rules))

def data(rules):
    return {}

def __str__():
    return ""

general =  (__str__,)