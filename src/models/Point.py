'''
module for Point class
'''
from threading import Lock


class Point:
    '''
    class responsible for storing and setting coordinates
    '''

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

        self._x_lock = Lock()
        self._y_lock = Lock()

    @property
    def coordinates(self):
        '''
        returns coordinates - tuple(x, y)
        '''
        with self._x_lock:
            with self._y_lock:
                return self._x, self._y

    @property
    def x(self):
        '''
        returns x coordinate
        '''
        with self._x_lock:
            return self._x

    @property
    def y(self):
        '''
        returns y coordinate
        '''
        with self._y_lock:
            return self._y

    def set_x(self, x):
        '''
        sets x coordinate
        '''
        with self._x_lock:
            self._x = x

    def set_y(self, y):
        '''
        sets y coordinate
        '''
        with self._y_lock:
            self._y = y
