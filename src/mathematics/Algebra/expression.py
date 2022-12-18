from ..Base.base import base, _arithmetic

class expression(base, _arithmetic):
    pass

class commutative(expression, tuple):
    pass

class nonCommutative(expression):
    pass
