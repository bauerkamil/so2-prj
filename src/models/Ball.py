'''
module for Ball class
'''
from threading import Thread
from time import sleep
from settings import Settings
from enums.player_numbers import PlayerNumber
from enums.direction import Direction
from managers.obstacle_manager import ObstacleManager
from managers.score_manager import ScoreManager
from models.point import Point


class Ball:
    '''
    class responsible for moving the ball and adding points to players
    '''

    def __init__(self, score: ScoreManager, obstacle_manager: ObstacleManager,
                 start_point: Point, direction: Direction, time_delay: float):
        self._time_delay = time_delay
        self._position = start_point
        self._score = score
        self._obstacle_manager = obstacle_manager

        self._is_running = False
        self._thread = Thread(target=self._move)
        self._direction = direction

    def run(self):
        '''
        runs the thread, which moves the ball
        '''
        self._is_running = True
        self._thread.start()

    def stop(self):
        '''
        stops the thread, which moves the ball
        '''
        self._is_running = False

    @property
    def is_running(self):
        '''
        returns true if ball is moving (thread is running)
        otherwise false
        '''
        return self._is_running

    @property
    def coordinates(self):
        '''
        returns current coordinates
        '''
        return self._position

    def _move(self):
        while self._is_running:
            sleep(self._time_delay)

            if not self._is_running:
                break

            x, y = self._position.coordinates

            player = self._player_got_point(self._position.x)
            if player is not None:
                self._score.add_point(player)
                self.stop()
                return

            self._direction = self._obstacle_manager.get_direction(
                self._position, self._direction)

            self._update_position(x, y)

    def _update_position(self, prev_x, prev_y):
        match self._direction:
            case Direction.UP_RIGHT:
                self._position.set_x(prev_x + 1)
                self._position.set_y(prev_y + 1)
            case Direction.UP_LEFT:
                self._position.set_x(prev_x - 1)
                self._position.set_y(prev_y + 1)
            case Direction.DOWN_RIGHT:
                self._position.set_x(prev_x + 1)
                self._position.set_y(prev_y - 1)
            case Direction.DOWN_LEFT:
                self._position.set_x(prev_x - 1)
                self._position.set_y(prev_y - 1)
            case _:
                raise ValueError("invalid direction")

    def _player_got_point(self, x_position):
        if x_position == 0:
            return PlayerNumber.ONE

        if x_position == Settings.MAP_WIDTH:
            return PlayerNumber.TWO

        return None
