from abc import abstractmethod
import types
from numbers import Number
from collections import OrderedDict
import inspect
from .rule import pattern

def lazy_fstring(string):
    globals_ = inspect.currentframe().f_back.f_globals.copy()
    locals_ = inspect.currentframe().f_back.f_locals.copy()
    return eval(f'f\'{string}\'', globals_, locals_)

# inspect.currentframe().f_back.f_globals.copy()
# inspect.currentframe().f_back.f_locals.copy()
def CAS_new(cls, *args, **kwargs):
    self = super(CAS, cls).__new__(cls)
    self.args = args
    self.kwargs = kwargs
    self = self.initialize(*args, **kwargs)    
    return self

def validate(data, kwdata, against):
    index=0
    for individual in against:
        match against[individual]:
            case 0:
                if not index<len(data) and individual not in kwdata:
                    return False
                else:
                    index+=1
            case 1:
                index = len(data)
            case 2:
                if individual not in kwdata:
                    return False
            case 4:
                pass
    return index==len(data)

def arguments_test(arguments):
    n=0
    for value in arguments.values():
        if type(value) is not int:
            return False
        if value>3:
            return False
        if n>0: 
            if (n%2) and value<=n:
                return False
            elif value<n:
                return False
        if value<0:
            return False
        if value<0:
            return False
        n=value
    return True


class CAS:
    exact: bool
    value: Number
    locals: list
    _globals: list = []
    def __new__(cls, *args, parent = None, locals = None, **kwargs):
        if hasattr(cls, 'arguments'):
            if not validate(args, kwargs, cls.arguments):
                raise ValueError('Invalid arguments for %s: %s, %s'%(cls.arguments, args, kwargs))
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
        return self._globals

    def __str__(self):
        try:
            temp = self.fstring%self.args
        except Exception:
            temp = self.fstring
        return lazy_fstring(temp)

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
    def __new__(cls, name:str, arguments:OrderedDict[str, int]|tuple[type, ...], **kwargs): #/, rules:tuple=(), initialize=lambda a, *b, **c:a, hardcode=lambda a, *b, **c:a, documentation:str='', parser=lambda s:s, OrderOfOperation=0):
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
        if 'initialize' not in kwargs:
            kwargs['initialize'] =lambda a, *b, **c: a
        if '__doc__' not in kwargs:
            kwargs['__doc__'] = ''
        if not arguments_test(arguments):
            raise ValueError('invalid argument selection')
        kwargs['arguments'] = arguments
        #parser, OrderOfOperations
        self = type.__new__(cls, name, (CAS,), kwargs)
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

    def initialize(self, name, parent = None, locals = None):
        self.locals = locals if locals is not None else []
        self.parent = parent
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
    exists = symbol('exists', OrderedDict(a=0), fstring =  '∃%s', latex_fstring = '\\exists{%s}')
    implies = symbol('implies', OrderedDict(a=0,b=0), fstring = '%s⇒%s', latex_fstring = '{%s\\implies{%s}}')
    land = symbol('land', OrderedDict(a=0,b=0), fstring='%s&%s', latex_fstring='{%s}\\land{%s}')
    commutative = pattern((symbol['A', 'B'], symbol['B', 'A']))
    symmetric = pattern((exists('A'), symbol['A', 'A']))
    transitive = pattern((land(symbol['A', 'B'], symbol['B', 'C']), symbol['A', 'C']))
    associative = pattern((symbol['A', symbol['B', 'C']], symbol[symbol['A', 'B'], 'C']))
    equality = symbol('equals',OrderedDict(a=0,b=0), fstring = '%s=%s', latex_fstring='{%s}={%s}', rules = (commutative, symmetric, transitive))
    addition = symbol('addition', OrderedDict(terms=1), fstring = '{chr(43).join(self.terms)}', latex_fstring = '{chr(43).join(self.terms)}', rules = (commutative, associative))
