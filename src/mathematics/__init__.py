'''
usefulpy-mathematics

A library to contain 

RELEASE NOTES:
0
 0.0
  Version 0.0.0:
   mathematics.py contains many mathematical functions.
  Version 0.0.1:
   An updated description and various bug fixes. Cleaner looking code with more
   comments.
  Version 0.0.2:
   Some small bug fixes
   Raises warnings at unfinished sections
 0.1
  Version 0.1.0
   Separated into sections and placed into a folder of its own
  Version 0.1.1
   Mostly some small bugfixes and clearer commenting throughout
  Version 0.1.2
   Several bugfixes, some work on algebraic solver and improvements on eq
  Version 0.1.3
   Heavy improvements in nmath, small bugfixes throughout
  Version 0.1.4
   Small improvement throughout.
 0.2
  Version 0.2.0
   Heavy bugfixing throughout. Deprecated algebraic solver and eq
  Version 0.2.1
   More bugfixing, some more functions. Efficiency increased
1
 1.0
# :-
  Version 1.0.0:
   Entirety of folder restructured. Much improved use of mathfuncs. Expression
   check has taken the place of eq and algebraic solver. Basic CAS implemented
   for the new mathfunc-eq-solver merge. Greater efficiency and power to most
   other areas. nmath made much smaller, most of its functionality has been
   moved to the mathfunc file.
  Version 1.0.1:
   Heavy bugfixing
 1.1
  Version 1.1.0:
   Remade CAS system. Moved things around to nmath.
2
 2.0
  Version 2.0.0:
   Seperated from main Usefulpython system.
'''
# CAS engine
# :  Structure pattern based definition of identities?
# :  :  Rule definition. 
# :  :  Global Rules, Function-tied rules, Numeric rules, and system rules. 
# :  Dynamic raising cos**2(x) = cos(x)**2
# :- sets
# :- Display
# :- GUI Box for input?
# :- Geometry
# :  :- Display
# :- Solver?
# :- Numeric Types
# :  :  Data-class like decorator for class definition?
# :  :  Basenum (Display for number type, not for actual storage)
# :  :  i = Number(CASvar(n), rules={n**2=-1})? 
# :  :  How does it infer rest of rules?
# :  :  Logic and set based definition of type? Quaternions = R(i, j, k), Matrix = R(m*n)?
# :  :- Quaternion 
# :  :  :  How does it infer orthonormalcy of ijk?
# :  :- Unit Type 
# :  :  :  enums?
# :  :  :  Subclass of Numeric Type?
# :  :- Boolean arithmetic definition?
# :  :  :  BoolType = (t, f, t+t = t, t+f = t, f+f = t, ~f = t, tt = t, tf = f, ff = f)?
# :- Vector, Matrix, Tensor?
# :  : Tensor-based systems of equations?
# Constants?


# Arithmetic Algebra
# :-- Symbol
# :-- Add
# :-- Mul
# :-- Pow
# :-- Factor
# :-- Polynomial
# HyperOperations
# :-- Tetration
# Functional Algebra
# :-- FunctionType
# :   :-- Explicit
# :   :-- Implicit
# :-- trig
# :-- log
# Calculus
# :-- partial
# :-- indefinite
# :-- Approx
# Numbers
# :-- Numberic
# :-- Baseview
# :-- Quaternion
# :-- Unit Type
# :-- Boolean type
# DiffEq
# :-- Laplace
# :-- Series
# :   :-- Taylor
# :   :-- Generating Functions
# :-- Fourier
# :-- ODE
# :   :-- Series
# :-- PDE
# Discrete
# :-- prod
# :-- sum
# Logic
# :-- in
# :-- for
# :-- and
# :-- or
# Sets
# :-- Self-Refering (...)
# :-- Sets
# System
# :-- Vector, Matrix, Tensor
# Geometry
# :-- System
# Solver
# :-- Equalities
# :-- Inequalities
# :-- Expresions
# :-- System
# :-- Symplify
# :-- HyperSymplify
# API
# :-- GUI
# :   :-- Plotting
# :   :-- Input
# :   :-- Display
# :   :-- Geometry
# :-- Unify
# :-- Calling
# :-- Printing
# :-- IDE
# Utils
# :-- Sorter
# :-- Random
# :-- cache
# :-- Errors
# :-- CasBase
# :-- Rules
# :-- Alphabets
# :-- Calldef?
# __init__
# __main__
# abc
# C/C++?
