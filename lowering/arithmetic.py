from core.node import Node


def const(value):

    node = Node(
        op="CONST",
        value=str(value)
    )

    node.origin = str(value)

    return node


def var(name):

    node = Node(
        op="VAR",
        value=name
    )

    node.origin = name

    return node


def eml(left, right):

    node = Node(
        op="EML",
        left=left,
        right=right
    )

    return node


def exp_eml(x):

    node = eml(
        x,
        const(1)
    )

    node.label = "exp"

    node.origin = f"exp({x.origin})"

    return node


def log_eml(x):

    node = eml(
        const(1),
        exp_eml(
            eml(
                const(1),
                x
            )
        )
    )

    node.label = "log"

    node.origin = f"log({x.origin})"

    return node


def subtract_eml(x, y):

    node = eml(
        log_eml(x),
        exp_eml(y)
    )

    node.label = "subtract"

    node.origin = f"({x.origin} - {y.origin})"

    return node


def minus_eml(x):

    node = subtract_eml(
        const(1),
        x
    )

    node.label = "negate"

    node.origin = f"-({x.origin})"

    return node


def plus_eml(x, y):

    node = subtract_eml(
        x,
        minus_eml(y)
    )

    node.label = "plus"

    node.origin = f"({x.origin} + {y.origin})"

    return node