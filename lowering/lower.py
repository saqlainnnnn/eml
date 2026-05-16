from sympy import *
from core.node import Node


def lower(expr):

    if expr.is_Number:
        return Node(op="CONST", value=str(expr))

    if expr.is_Symbol:
        return Node(op="VAR", value=str(expr))

    if isinstance(expr, Add):
        args = expr.args

        return Node(
            op="ADD",
            left=lower(args[0]),
            right=lower(args[1])
        )

    if isinstance(expr, Mul):
        args = expr.args

        return Node(
            op="MUL",
            left=lower(args[0]),
            right=lower(args[1])
        )

    if isinstance(expr, Pow):

        return Node(
            op="POW",
            left=lower(expr.base),
            right=lower(expr.exp)
        )

    if expr.func == sin:

        return Node(
            op="SIN",
            left=lower(expr.args[0])
        )

    raise NotImplementedError(f"Unsupported expression: {expr}")