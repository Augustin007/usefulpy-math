from expression import commutative

class add(commutative):
    def __str__(self, /)->str:
        return '+'.join(map(str, self)).replace('+-', '-')
    
    def tex(self, /)->str:
        pass