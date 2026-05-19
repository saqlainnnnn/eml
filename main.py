from lowering.arithmetic import *
from visualize.tree_view import show


x = var("x")

expr = divide_eml(
    x,
    x
)

show(expr)