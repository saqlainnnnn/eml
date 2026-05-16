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

def multiply_eml(x, y):

    node = exp_eml(

        plus_eml(

            log_eml(x),

            log_eml(y)
        )
    )

    node.label = "multiply"

    node.origin = f"({x.origin} * {y.origin})"

    return node

def inverse_eml(x):

    node = exp_eml(

        minus_eml(

            log_eml(x)
        )
    )

    node.label = "inverse"

    node.origin = f"(1 / {x.origin})"

    return node


def divide_eml(x, y):

    node = multiply_eml( x,inverse_eml(y))

    node.label = "divide"

    node.origin = f"({x.origin} / {y.origin})"

    return node

def power_eml(x, y):

    node = exp_eml(multiply_eml(y,log_eml(x)))

    node.label = "power"

    node.origin = f"({x.origin} ^ {y.origin})"

    return node

def sqrt_eml(x):

    node = exp_eml(

        divide_eml(

            log_eml(x),

            const(2)
        )
    )

    node.label = "sqrt"

    node.origin = f"sqrt({x.origin})"

    return node

def half_eml(x):

    node = divide_eml(

        x,

        const(2)
    )

    node.label = "half"

    node.origin = f"({x.origin} / 2)"

    return node


def average_eml(x, y):

    node = half_eml(

        plus_eml(x, y)
    )

    node.label = "average"

    node.origin = f"avg({x.origin}, {y.origin})"

    return node