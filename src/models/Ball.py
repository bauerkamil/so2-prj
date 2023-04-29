from threading import Thread
from time import sleep
from managers.ObstacleManager import ObstacleManager
from enums.Direction import Direction
from models.Point import Point
from managers.ScoreManager import ScoreManager


class Ball:
    def __init__(self, score: ScoreManager, obstacle_manager: ObstacleManager, start_point: Point, direction: Direction, time_delay: float):
        self._time_delay = time_delay
        self._position = start_point
        self._score = score
        self._obstacle_manager = obstacle_manager

        self._is_running = False
        self._thread = Thread(target=self._move)
        self._direction = direction

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

            player = self._obstacle_manager.player_got_point(self._position.x)
            if player != None:
                self._score.add_point(player)
                self.stop()
                return

            self._direction = self._obstacle_manager.get_direction(
                self._position, self._direction)

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
