from rich.tree import Tree
from rich import print
from domains.render import render_constraint


def truncate(text, limit=40):

    if text is None:
        return ""

    text = str(text)

    if len(text) > limit:
        return text[:limit] + "..."

    return text


def build_label(node):

    parts = []

    # neon structural colors
    op_colors = {
        "EML": "bold bright_cyan",
        "CONST": "bold bright_yellow",
        "VAR": "bold bright_green"
    }

    op_style = op_colors.get(
        node.op,
        "bold bright_white"
    )

    # operation name
    parts.append(
        f"[{op_style}]"
        f"{node.op}"
        f"[/{op_style}]"
    )

    # neon node ids
    parts.append(
    f"[white][{node.id}][/white]"
)

    if node.hash:

        parts.append(
            f"[dim cyan]{node.hash}[/dim cyan]"
    )

    # semantic operation families
    semantic_colors = {

        # arithmetic
        "plus": "black on bright_green",
        "subtract": "black on bright_green",
        "multiply": "black on bright_green",
        "divide": "black on bright_green",
        "negate": "black on bright_green",
        "power": "black on bright_green",
        "half": "black on bright_green",
        "average": "black on bright_green",

        # logarithmic / exponential
        "log": "black on bright_magenta",
        "exp": "black on bright_magenta",

        # trigonometric
        "sin": "black on bright_blue",
        "cos": "black on bright_blue",
        "tan": "black on bright_blue",

        # hyperbolic
        "sinh": "black on bright_cyan",
        "cosh": "black on bright_cyan",
        "tanh": "black on bright_cyan",

        # inverse trig
        "arcsin": "black on bright_red",
        "arccos": "black on bright_red",
        "arctan": "black on bright_red",

        # complex
        "imaginary": "black on bright_yellow",

        # roots
        "sqrt": "black on bright_white"
    }

    # semantic label box
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

            value_style = "bold bright_blue"

        elif node.op == "VAR":

            value_style = "bold bright_green"

        else:

            value_style = "bold bright_white"

        parts.append(
            f"[{value_style}]"
            f"{node.value}"
            f"[/{value_style}]"
        )

    # domains
    if node.constraints:

        constraint_text = " ∧ ".join(
            render_constraint(c)
            for c in node.constraints
        )

        parts.append(
            f"[bright_red]"
            f"{truncate(constraint_text, 60)}"
            f"[/bright_red]"
        )

    # reconstructed expression
    if node.origin:

        parts.append(
            f"[bright_green]"
            f"{truncate(node.origin)}"
            f"[/bright_green]"
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