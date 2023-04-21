from threading import Thread
from time import sleep
import random
from Board import Board
from enums.Direction import Direction
from Point import Point
from Score import Score
from enums.Players import Player


class Ball:
    def __init__(self, score: Score, board: Board, start_point: Point, time_delay):
        self._time_delay = time_delay
        self._position = start_point
        self._score = score
        self._board = board 

        self._is_running = False
        self._thread = Thread(target=self._move)
        self._direction = random.choice(list(Direction))

    def run(self):
        self._is_running = True
        self._thread.start()

    def stop(self):
        self._is_running = False

    @property
    def is_running(self):
        return self._is_running

    @property
    def coordinates(self):
        return self._position
    
    def set_direction(self, direction: Direction):
        self._direction = direction
    
    def _move(self):
        while self._is_running:
            sleep(self._time_delay)
            x, y = self._position.coordinates
            
            match self._direction:
                case Direction.UP_RIGHT:
                    self._position.set_x(x + 1)
                    self._position.set_y(y + 1)
                case Direction.UP_LEFT:
                    self._position.set_x(x - 1)
                    self._position.set_y(y + 1)
                case Direction.DOWN_RIGHT:
                    self._position.set_x(x + 1)
                    self._position.set_y(y - 1)
                case Direction.DOWN_LEFT:
                    self._position.set_x(x - 1)
                    self._position.set_y(y - 1)
            
            self._direction = self._board.get_direction(self._position, self._direction)

            player = self._board.player_got_point(self._position.x)
            if player != None:
                self._score.add_point(player)
                self.stop()

            print(self._thread, self._position.coordinates, self._direction)
    