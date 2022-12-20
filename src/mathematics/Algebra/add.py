from expression import commutative

class add(commutative):
    def __new__(cls, name, *args):
        self = tuple.__new__(cls, name, args)
        # subrules = cls
    def __str__(self, /)->str:
        return '+'.join(map(str, self)).replace('+-', '-')
    
    def tex(self, /)->str:
        pass

    def substitute(self, data: dict, /):
        pass