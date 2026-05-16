from core.node import Node


def const(value):
    return Node(
        op="CONST",
        value=str(value)
    )


def var(name):
    return Node(
        op="VAR",
        value=name
    )


def eml(left, right):
    return Node(
        op="EML",
        left=left,
        right=right
    )


def exp_eml(x):
    return eml(x, const(1))


def log_eml(x):
    return eml(const(1),exp_eml(eml(const(1),x)))

def subtract_eml(x, y):
    return eml(log_eml(x),exp_eml(y))

def minus_eml(x):
    return subtract_eml(const(1),x)


def plus_eml(x, y):
    return subtract_eml(x,minus_eml(y))