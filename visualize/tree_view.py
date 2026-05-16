from rich.tree import Tree
from rich import print


def truncate(text, limit=40):

    if text is None:
        return ""

    text = str(text)

    if len(text) > limit:
        return text[:limit] + "..."

    return text


def build_label(node):

    parts = []

    # structural node colors
    op_colors = {
        "EML": "bold cyan",
        "CONST": "bold yellow",
        "VAR": "bold green"
    }

    op_style = op_colors.get(
        node.op,
        "bold white"
    )

    # operation name
    parts.append(
        f"[{op_style}]"
        f"{node.op}"
        f"[/{op_style}]"
    )

    # node id
    parts.append(
        f"[dim white][{node.id}][/dim white]"
    )

    # semantic operation family colors
    semantic_colors = {

        # arithmetic
        "plus": "black on bright_green",
        "subtract": "black on bright_green",
        "multiply": "black on bright_green",
        "divide": "black on bright_green",
        "negate": "black on bright_green",
        "power": "black on bright_green",

        # logarithmic / exponential
        "log": "black on magenta",
        "exp": "black on magenta",

        # trigonometric
        "sin": "black on bright_blue",
        "cos": "black on bright_blue",
        "tan": "black on bright_blue",

        # hyperbolic
        "sinh": "black on cyan",
        "cosh": "black on cyan",
        "tanh": "black on cyan",

        # inverse trig
        "arcsin": "black on bright_red",
        "arccos": "black on bright_red",
        "arctan": "black on bright_red"
    }

    # semantic label
    if node.label:

        semantic_style = semantic_colors.get(
            node.label,
            "black on white"
        )

        semantic = (
            f"[{semantic_style}] "
            f"{node.label} "
            f"[/{semantic_style}]"
        )

        parts.append(semantic)

    # values
    if node.value:

        if node.op == "CONST":

            value_style = "bold yellow"

        elif node.op == "VAR":

            value_style = "bold green"

        else:

            value_style = "bold white"

        parts.append(
            f"[{value_style}]"
            f"{node.value}"
            f"[/{value_style}]"
        )

    # reconstructed expression
    if node.origin:

        parts.append(
            f"[green]"
            f"{truncate(node.origin)}"
            f"[/green]"
        )

    return " ".join(parts)


def build_tree(node):

    tree = Tree(
        build_label(node)
    )

    if node.left:
        tree.add(
            build_tree(node.left)
        )

    if node.right:
        tree.add(
            build_tree(node.right)
        )

    return tree


def show(node):

    print(
        build_tree(node)
    )