from dataclasses import dataclass, field


@dataclass
class Node:

    kind: str

    inputs: list["Node"] = field(
        default_factory=list
    )

    attrs: dict = field(
        default_factory=dict
    )

    metadata: dict = field(
        default_factory=dict
    )