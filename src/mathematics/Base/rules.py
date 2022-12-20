import types

# 

class rule:
    def __init__(self, functionality):
        self.functionality = functionality
    
    def apply(self, to):
        original = to
        new = self.functionality(original)
        return new if original != new else None

class ruleGroup(tuple):
    def apply(self, to):
        for n in self:
            new = n.apply(to)
            if new is not None:
                return new
        return None
