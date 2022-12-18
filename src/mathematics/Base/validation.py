
from collections import OrderedDict
from decimal import Decimal
from fractions import Fraction
from numbers import Number
import typing

constants = (int, float, complex, Decimal, Fraction, Number)
Rationals = (int, Fraction)
MathAttributes = ('__add__', '__radd__', '__sub__', '__mul__', '__rsub__', '__rmul__',
                  '__truediv__', '__rtruediv__', '__pow__', '__rpow__')


def isConstant(n: typing.Any) -> bool:
    '''isConstant

    Check whether a number is constant for cas engine

    Parameters
    ----------
    n : typing.Any
        Number to be checked

    Returns
    -------
    bool
    '''
    if isinstance(n, constants):
        return True
    if hasattr(n, 'exact'):
        return bool(n.exact)
    return all(map(lambda x: hasattr(n, x), MathAttributes))


def isRational(n: typing.Any) -> bool:
    '''isRational

    Check whether n is rational for cas engine

    Parameters
    ----------
    n : typing.Any
        Number to be checked

    Returns
    -------
    bool
    '''
    ''''''
    if isinstance(n, (Rationals)):
        return True
    if hasattr(n, 'rational'):
        return bool(n.rational)
    return False


def isExact(n: typing.Any) -> bool:
    '''isExact

    Check whether a number is stored 'exactly' in the engine

    Parameters
    ----------
    n : typing.Any
        Number to be checked

    Returns
    -------
    bool
    '''
    if isRational(n):
        return True
    if hasattr(n, 'exact'):
        return bool(n.exact)
    return False

def removeDuplicates(tup: tuple) -> tuple:
    '''removeDuplicates

    Remove duplicates

    Parameters
    ----------
    tup : tuple
        Original values of iterable

    Returns
    -------
    tuple
        New tuple with duplicates removed
    '''
    return tuple(OrderedDict.fromkeys(tup).keys())


def getArgs(args, selector):
    '''get args according to selector'''
    return [args[select] for select in selector]


def getValue(n):
    if hasattr(n, 'value') and n.value is not None:
        return n.value
    return n


def distribute(expression):
    '''distribute

    Propogate distribution in CAS

    Parameters
    ----------
    expression : CASobject
        Point in distribution

    Returns
    -------
    CASobject
        New expression re-distributed
    '''
    if hasattr(expression, 'distribute'):
        return expression.distribute()
    return expression

def substitute(expression, data:dict):
    '''substitute

    Propogate distribution in CAS

    Parameters
    ----------
    expression : CASobject
        Point in distribution
    data : dict
        Substitutions
    Returns
    -------
    CASobject
        New expression re-distributed
    '''
    if hasattr(expression, 'distribute'):
        return expression.distribute()
    return expression
