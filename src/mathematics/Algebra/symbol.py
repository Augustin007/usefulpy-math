
from ..Base.base import base, _arithmetic
from ..Base.rules import rule, ruleGroup

class symbol(base, _arithmetic):
    classRules = ruleGroup()
    __slots__ = ['name', 'texstr']
    def __init__(self, name: str, tex: str = ""):
        self.name: str = name
        if not tex:
            tex = name
        self.texstr: str = tex

    def __str__(self, /) -> str:
        return self.name
    
    def tex(self, /) -> str:
        return self.texstr

    def __eq__(self, other, /)-> bool:
        return self is other
    
    def substitute(self, data: dict, /):
        return data.get(self, self)