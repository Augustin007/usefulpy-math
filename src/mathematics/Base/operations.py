from .base import symbol, CAS
from .rule import pattern
from collections import OrderedDict

exists = symbol('exists', OrderedDict(a=0), fstring =  '∃%s', latex_fstring = '\\exists{%s}')
#uniqueExists
implies = symbol('implies', OrderedDict(a=0,b=0), fstring = '%s⇒%s', latex_fstring = '{%s\\implies{%s}}')
land = symbol('land', OrderedDict(a=0,b=0), fstring='%s&%s', latex_fstring='{%s}\\land{%s}')
lnot = symbol('lnot', OrderedDict(a=0))
lni = symbol('lni', OrderedDict(a=0,b=0))
lin = symbol('lin', OrderedDict(a=0, b=0))
#lor, implimented as a functional generic combination of land and lnot? along with lnand, lnor, lxand, and lxor.
zfcset = symbol('zfcset', OrderedDict(a=2))
#zfcset definition?
# typeinferrence
# Generic number type generated from a subset given certain qualities
# dual_numbers = number.create('dual numbers', 'a+bε').a_in(R).b_in(R).ε_ni('ε**2==0 & ε!=0')
#other sets
#type theory? zfcset

commutative = pattern((symbol['A', 'B'], symbol['B', 'A']))
symmetric = pattern((exists('A'), symbol['A', 'A']))
transitive = pattern((land(symbol['A', 'B'], symbol['B', 'C']), symbol['A', 'C']))
associative = pattern((symbol['A', symbol['B', 'C']], symbol[symbol['A', 'B'], 'C']))

equality = symbol('equals',OrderedDict(a=0,b=0), fstring = '%s=%s', latex_fstring='{%s}={%s}', rules = (commutative, symmetric, transitive))
addition = symbol('addition', OrderedDict(terms=1), fstring = '{chr(43).join(self.terms)}', latex_fstring = '{chr(43).join(self.terms)}', rules = (commutative, associative))
