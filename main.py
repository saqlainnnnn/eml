from lowering.arithmetic import *
from visualize.tree_view import show


x = var("x")
y = var("y")

tree = sqrt_eml(
    log_eml(
        divide_eml(x, y)
    )
)

show(tree)