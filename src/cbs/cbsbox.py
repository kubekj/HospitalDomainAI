from typing import Tuple

import numpy as np

from src.utils.color import Color


class CBSBox:
    def __init__(self, label: chr, position: Tuple[int, int], goal: Tuple[int, int], color: Color):
        self.label = label  # Box identifier (A, B, C, ...)
        self.position = np.array(position, dtype=int)
        self.goal = np.array(goal, dtype=int)
        self.color = color

    def move(self, delta_row, delta_col):
        self.position += np.array([delta_row, delta_col])

    def is_at_goal(self):
        return np.array_equal(self.position, self.goal)

    def __eq__(self, other):
        if not isinstance(other, CBSBox):
            return NotImplemented
        return self.label == other.label and np.array_equal(self.position, other.position)

    def __hash__(self):
        return hash((self.label, tuple(self.position)))

    def __repr__(self):
        return f"Box {self.label} at {self.position.tolist()}"
