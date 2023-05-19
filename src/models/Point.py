from threading import Lock


class Point:

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

        self._x_lock = Lock()
        self._y_lock = Lock()

    @property
    def coordinates(self):
        with self._x_lock:
            with self._y_lock:
                return self._x, self._y

    @property
    def x(self):
        with self._x_lock:
            return self._x

    @property
    def y(self):
        with self._y_lock:
            return self._y

    def set_x(self, x):
        with self._x_lock:
            self._x = x

    def set_y(self, y):
        with self._y_lock:
            self._y = y
