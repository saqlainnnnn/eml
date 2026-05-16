from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    op: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    value: Optional[str] = None

    def is_leaf(self):
        return self.value is not None