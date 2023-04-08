from threading import Thread
from time import sleep
import random
from Score import Score


class Ball:
    def __init__(self, score: Score, start_x, start_y, time_delay):
        self._time_delay = time_delay
        self._x = start_x
        self._y = start_y

        self._is_running = False
        self._thread = Thread(target=self._move)
        self._vect_x = random.randint(0,1)*2-1
        self._vect_y = random.randint(-1,1)

    def run(self):
        self._is_running = True
        self._thread.start()

    def stop(self):
        self._is_running = False

    @property
    def get_is_running(self):
        return self._is_running

    @property
    def get_coordinates(self):
        return (self._x, self._y)
    
    def set_vector(self, x, y):
        self._vect_x = x
        self._vect_y = y
    
    def _move(self):
        while self._is_running:
            sleep(self._time_delay)
            self._x += self._vect_x
            self._y += self._vect_y

            print(self._thread, self._x, self._y)
    