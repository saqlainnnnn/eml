def simplify_predicate(node):

    if (
        node.left
        and node.right
        and node.left.is_leaf()
        and node.right.is_leaf()
    ):

        try:

            left = float(node.left.value)
            right = float(node.right.value)

            if node.op == "GT":
                return left > right

            if node.op == "GTE":
                return left >= right

            if node.op == "LT":
                return left < right

            if node.op == "LTE":
                return left <= right

            if node.op == "EQ":
                return left == right

            if node.op == "NEQ":
                return left != right

        except:
            pass

    return node