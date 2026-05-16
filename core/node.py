from dataclasses import dataclass, field
from typing import Optional
import uuid
import hashlib


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

    hash: Optional[str] = None

    def is_leaf(self):
        return self.value is not None

    def compute_hash(self):

        left_hash = (
            self.left.hash
            if self.left else ""
        )

        right_hash = (
            self.right.hash
            if self.right else ""
        )

        raw = (
            f"{self.op}|"
            f"{self.value}|"
            f"{left_hash}|"
            f"{right_hash}"
        )

        self.hash = hashlib.md5(
            raw.encode()
        ).hexdigest()[:8]

        return self.hash