from abc import abstractmethod
import types
from numbers import Number

def CAS_new(cls, *args, **kwargs):
    self = super(CAS, cls).__new__(cls)
    self.args = args
    self.kwargs = kwargs
    self = self.initialize(*args, **kwargs)    
    return self

class CAS:
    exact: bool
    value: Number
    locals: list
    _globals: list = []
    def __new__(cls, *args, parent = None, locals = None, **kwargs):
        # argument validation?
        self = CAS_new(cls, *args, **kwargs)
        if locals is None:
            locals = []
        self.locals = locals
        self.locals.append(self)
        self.parent = parent
        return self
    
    @property
    def globals(self):
        if self.parent is not None:
            return self.parent.locals + self.parent.globals
        return self.globals_

    def __str__(self):
        try:
            temp = self.fstring%self.args
        except:
            temp = self.fstring
        return temp.format(self.args, self.kwargs)

    def __repr__(self):
        return f'CAS[\'{self}\']'

    def __class_getitem__(self, expression):
        pass


class SymbolAlias(types.GenericAlias):
    def __new__(cls, expression):
        return types.GenericAlias.__new__(cls, expression)


class symbol(type):
    '''symbol 
    Stores symbols with meaning.
    '''
    def __new__(cls, name:str, format:str, latex:str, arguments:tuple[tuple[str, type, int], ...], /, rules:tuple=(), initialize=lambda a, *b, **c:a, hardcode=lambda a, *b, **c:a, documentation:str='', parser=lambda s:s, OrderOfOperation=0):
        '''__new__

        Creates a new symbol for the CAS engine

        Use example:
        exists = symbol('exists', '∃%s', '\exists{%s}', 1, initialize=variable)
        implies = symbol('implies', '%s⇒%s', '{%s\implies{%s}}, 2, hardcode=imply)
        commutative = implies(symbol['A', 'B'], symbol['B', 'A'])
        symmetric = implies(exists('A'), symbol['A', 'A'])
        transitive = implies(symbol['A', 'B'] & symbol['B', 'C'], symbol['A', 'C'])
        equality = symbol('=', '%s=$s', 2, rules = (commutative, symmetric, transitive))

        Parameters
        ----------
        Unicode : str
            Character to represent it
        format : str
            formatable string for arguments to generate IDE display
        latex : str
            formatable string for arguments to generate latex code
        arguments : int|tuple[type, ...]|tuple[str, ...]
            number of arguments of new symbol, or more complicated argument code, or argument names
        rules : tuple, optional
            A tuple containing the applicable rules, by default ()
        initialize : callable, optional
            called at the end of initialization by default lambda*a:None
        hardcode : callable, optional
            hardcoded application, by default lambda*a:None
        documentation : str
            documentation of instance.
        ''' # Maybe have it define a new type? Order of operations (or is that in parsing, I guess, nesting gives us order here, that's notational?) Unicode symbol is for... what, exactly?
        namespace = {'initialize':initialize, 'hardcode':hardcode, '__doc__':documentation, 'arguments':arguments,'rules':rules, 'fstring':format, 'latex_fstring':latex, 'parser':parser, 'OrderOfOperations':OrderOfOperation}
        self = type.__new__(cls, name, (CAS,), namespace)
        return self
    
    def __init__(self, *args, **kwargs):
        pass

 
    def __class_getitem__(self, key):
        return types.GenericAlias(self, key)

class variable(CAS):
    '''variable _summary_

    Parameters
    ----------
    CASbase : _type_
        _description_
    '''

    __slots__ = {'name':str}

    def initialize(self, name):
        self.fstring = name
        self.name = name
        return self

class function(CAS):
    '''function _summary_

    Parameters
    ----------
    CASbase : _type_
        _description_
    '''    
    pass

if __name__ == '__main__':
    exists = symbol('exists', '∃%s', '\exists{%s}', (('a', int, 0),))#, initialize=variable)
    implies = symbol('implies', '%s⇒%s', '{%s\implies{%s}}', (('a', int, 0), ('b', int, 0)))#, hardcode=imply)
    land = symbol('land', '%s&%s', '{%s}\land{%s}', (('a', int, 0),('b', int, 0)))
    commutative = implies(symbol['A', 'B'], symbol['B', 'A'], locals = CAS._globals)
    symmetric = implies(exists('A'), symbol['A', 'A'], locals = CAS._globals)
    transitive = implies(land(symbol['A', 'B'], symbol['B', 'C']), symbol['A', 'C'], locals = CAS._globals)
    equality = symbol('equals', '%s=%s', '{%s}={%s}', (('a', int, 0), ('b', int, 0)), rules = (commutative, symmetric, transitive))
