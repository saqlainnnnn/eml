from sympy import *
from lowering.arithmetic import *


def lower(expr):

    # constants
    if expr.is_Number:
        return const(expr)

    # variables
    if expr.is_Symbol:
        return var(str(expr))

    # logarithm
    if expr.func == log:
        return log_eml(
            lower(expr.args[0])
        )

    # exponential
    if expr.func == exp:
        return exp_eml(
            lower(expr.args[0])
        )

    raise NotImplementedError(
        f"Unsupported expression: {expr}"
    )