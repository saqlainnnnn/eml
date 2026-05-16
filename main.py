from sympy import symbols, sin
from lowering.lower import lower
from visualize.tree_view import show


x = symbols("x")

expr = x**2 + sin(x)

tree = lower(expr)

show(tree)