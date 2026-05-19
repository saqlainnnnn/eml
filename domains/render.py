def render_constraint(node):

    if node.op == "GT":
        return (
            f"{node.left.origin} > "
            f"{node.right.origin}"
        )

    if node.op == "GTE":
        return (
            f"{node.left.origin} >= "
            f"{node.right.origin}"
        )

    if node.op == "LT":
        return (
            f"{node.left.origin} < "
            f"{node.right.origin}"
        )

    if node.op == "LTE":
        return (
            f"{node.left.origin} <= "
            f"{node.right.origin}"
        )

    if node.op == "EQ":
        return (
            f"{node.left.origin} == "
            f"{node.right.origin}"
        )

    if node.op == "NEQ":
        return (
            f"{node.left.origin} != "
            f"{node.right.origin}"
        )

    return node.op