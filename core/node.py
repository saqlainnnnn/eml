from dataclasses import dataclass, field
from typing import Optional
import uuid


@dataclass
class Node:
    op: str

    left: Optional["Node"] = None
    right: Optional["Node"] = None

    value: Optional[str] = None

    label: Optional[str] = None
    origin: Optional[str] = None

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())[:8]
    )

    def is_leaf(self):
        return self.value is not None