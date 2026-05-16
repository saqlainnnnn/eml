from rich.tree import Tree
from rich import print


def build_tree(node):

    label = node.op

    if node.value:
        label += f": {node.value}"

    tree = Tree(label)

    if node.left:
        tree.add(build_tree(node.left))

    if node.right:
        tree.add(build_tree(node.right))

    return tree


def show(node):
    print(build_tree(node))