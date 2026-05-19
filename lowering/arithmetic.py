from core.node import Node
from core.cache import NODE_CACHE


def const(value):

    temp = Node(
        op="CONST",
        value=str(value)
    )

    temp.origin = str(value)

    temp.compute_hash()

    if temp.hash in NODE_CACHE:
        return NODE_CACHE[temp.hash]

    NODE_CACHE[temp.hash] = temp

    return temp

def var(name):

    temp = Node(
        op="VAR",
        value=name
    )

    temp.origin = name

    temp.compute_hash()

    if temp.hash in NODE_CACHE:
        return NODE_CACHE[temp.hash]

    NODE_CACHE[temp.hash] = temp

    return temp

def eml(left, right):

    temp = Node(
        op="EML",
        left=left,
        right=right
    )

    temp.compute_hash()

    if temp.hash in NODE_CACHE:
        return NODE_CACHE[temp.hash]

    NODE_CACHE[temp.hash] = temp

    return temp

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

    node.domains.extend(
        x.domains
    )

    node.domains.append(
        f"{x.origin} > 0"
    )

    node.domains = list(
        set(node.domains)
    )

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

    node.domains.extend(
        x.domains
    )

    node.domains.append(
        f"{x.origin} != 0"
    )

    node.domains = list(
        set(node.domains)
    )

    return node


def divide_eml(x, y):

    node = multiply_eml( x,inverse_eml(y))

    node.label = "divide"

    node.origin = f"({x.origin} / {y.origin})"

    node.domains.extend(
        x.domains
    )

    node.domains.extend(
        y.domains
    )

    node.domains.append(
        f"{y.origin} != 0"
    )

    node.domains = list(
        set(node.domains)
    )

    return node

def power_eml(x, y):

    node = exp_eml(multiply_eml(y,log_eml(x)))

    node.label = "power"

    node.origin = f"({x.origin} ^ {y.origin})"

    node.domains.extend(
        x.domains
    )

    node.domains.extend(
        y.domains
    )

    node.domains.append(
        f"{x.origin} > 0"
    )

    node.domains = list(
        set(node.domains)
    )

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

    node.domains.extend(
        x.domains
    )

    node.domains.append(
        f"{x.origin} >= 0"
    )

    node.domains = list(
        set(node.domains)
    )

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

def i_eml():

    node = exp_eml(

        divide_eml(

            log_eml(
                minus_eml(
                    const(1)
                )
            ),

            const(2)
        )
    )

    node.label = "imaginary"

    node.origin = "i"

    return node

def cosh_eml(x):

    node = half_eml(

        plus_eml(

            exp_eml(x),

            exp_eml(
                minus_eml(x)
            )
        )
    )

    node.label = "cosh"

    node.origin = f"cosh({x.origin})"

    return node

def sinh_eml(x):

    node = half_eml(

        subtract_eml(

            exp_eml(x),

            exp_eml(
                minus_eml(x)
            )
        )
    )

    node.label = "sinh"

    node.origin = f"sinh({x.origin})"

    return node


def tanh_eml(x):

    node = divide_eml(

        sinh_eml(x),

        cosh_eml(x)
    )

    node.label = "tanh"

    node.origin = f"tanh({x.origin})"

    node.domains.extend(
        x.domains
    )

    node.domains.append(
        f"cos({x.origin}) != 0"
    )

    node.domains = list(
        set(node.domains)
    )

    return node

def cos_eml(x):

    node = cosh_eml(

        divide_eml(

            x,

            i_eml()
        )
    )

    node.label = "cos"

    node.origin = f"cos({x.origin})"

    return node

def pi_eml():

    node = divide_eml(

        log_eml(
            minus_eml(
                const(1)
            )
        ),

        i_eml()
    )

    node.label = "pi"

    node.origin = "pi"

    return node

def sin_eml(x):

    node = cos_eml(

        subtract_eml(

            x,

            half_eml(
                pi_eml()
            )
        )
    )

    node.label = "sin"

    node.origin = f"sin({x.origin})"

    return node

def tan_eml(x):

    node = divide_eml(

        sin_eml(x),

        cos_eml(x)
    )

    node.label = "tan"

    node.origin = f"tan({x.origin})"

    return node

def arsinh_eml(x):

    node = log_eml(

        plus_eml(

            x,

            sqrt_eml(

                plus_eml(

                    const(1),

                    power_eml(
                        x,
                        const(2)
                    )
                )
            )
        )
    )

    node.label = "arsinh"

    node.origin = f"arsinh({x.origin})"

    return node

def arcosh_eml(x):

    node = log_eml(

        plus_eml(

            x,

            sqrt_eml(

                subtract_eml(

                    power_eml(
                        x,
                        const(2)
                    ),

                    const(1)
                )
            )
        )
    )

    node.label = "arcosh"

    node.origin = f"arcosh({x.origin})"

    return node

def arctanh_eml(x):

    node = half_eml(

        log_eml(

            divide_eml(

                plus_eml(
                    const(1),
                    x
                ),

                subtract_eml(
                    const(1),
                    x
                )
            )
        )
    )

    node.label = "arctanh"

    node.origin = f"arctanh({x.origin})"

    node.domains.extend(
        x.domains
    )

    node.domains.append(
        f"{x.origin} > -1"
    )

    node.domains.append(
        f"{x.origin} < 1"
    )

    node.domains = list(
        set(node.domains)
)

    return node