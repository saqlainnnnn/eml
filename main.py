from core.node import Node

from core.serialize import to_json


x = Node(
    kind="leaf",
    attrs={
        "symbol": "x"
    }
)

y = Node(
    kind="leaf",
    attrs={
        "symbol": "y"
    }
)

expr = Node(
    kind="merge",
    inputs=[x, y]
)

print(
    to_json(expr)
)