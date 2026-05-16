from lowering.arithmetic import *
from visualize.tree_view import show


x = var("x")

tree = arctanh_eml(x)

show(tree)