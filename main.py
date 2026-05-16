from lowering.arithmetic import *
from visualize.tree_view import show


x = var("x")
y = var("y")

tree = plus_eml(x, y)

show(tree)