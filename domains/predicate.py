from core.node import Node
from core.cache import NODE_CACHE


def predicate(op, left, right):

    temp = Node(
        op=op,
        left=left,
        right=right
    )

    print(
        f"[PREDICATE CREATED] "
        f"{temp.op} "
        f"{left.origin} "
        f"{right.origin}"
    )

    temp.compute_hash()

    if temp.hash in NODE_CACHE:
        return NODE_CACHE[temp.hash]

    NODE_CACHE[temp.hash] = temp

    return temp


def gt(x, y):
    return predicate("GT", x, y)


def gte(x, y):
    return predicate("GTE", x, y)


def lt(x, y):
    return predicate("LT", x, y)


def lte(x, y):
    return predicate("LTE", x, y)


def eq(x, y):
    return predicate("EQ", x, y)


def neq(x, y):
    return predicate("NEQ", x, y)