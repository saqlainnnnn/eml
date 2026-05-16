from sympy import symbols, log
from lowering.lower import lower
from visualize.tree_view import show


x = symbols("x")

expr = log(x)

tree = lower(expr)

show(tree)