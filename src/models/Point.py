



class Point:

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
    
    @property
    def coordinates(self):
        return self._x, self._y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y