
from Direction import Direction

class Board:

    def __init__(self, size_x, size_y):
        self._size_x = size_x
        self._size_y = size_y
        self._obstacles = []

    def get_direction(self, x, y):
        return Direction.DOWN
