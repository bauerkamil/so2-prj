
'''
module for BallManager class
'''
import random
from threading import Lock, Thread
from time import sleep
from models.ball import Ball
from models.point import Point
from managers.score_manager import ScoreManager
from managers.obstacle_manager import ObstacleManager
from enums.direction import Direction
from settings import Settings


class BallManager:
    '''
    class responsible for storing and generating new balls
    '''

    def __init__(self, obstacle_manager: ObstacleManager, score_manager: ScoreManager):
        self._obstacle_manager = obstacle_manager
        self._score_manager = score_manager
        self._time_delay = Settings.BALL_SPAWN_TIME
        self._is_running = False
        self._thread = Thread(target=self._generate_balls)
        self._lock = Lock()
        point = Point(
            random.randint(0.2 * Settings.MAP_WIDTH,
                           0.8 * Settings.MAP_WIDTH),
            random.randint(0.2 * Settings.MAP_HEIGHT,
                           0.8 * Settings.MAP_HEIGHT))
        self._balls = [
            Ball(score_manager, obstacle_manager, point,
                 random.choice(list(Direction)), 0.2)
        ]

    @property
    def balls_coordinates(self):
        '''
        returns an array of coordinates for balls
        '''
        with self._lock:
            return [ball.coordinates.coordinates for ball in self._balls]

    def refresh_running_balls(self):
        '''
        removes balls that are not active
        '''
        with self._lock:
            self._balls = list(filter(lambda x: (x.is_running), self._balls))

    def run(self):
        '''
        runs the thread, which generates balls
        '''
        self._is_running = True
        self._thread.start()
        self._run_balls()

    def stop(self):
        '''
        stops the thread, which generates balls
        '''
        self._is_running = False
        self._stop_balls()

    def _generate_balls(self):
        while self._is_running:
            sleep(self._time_delay)

            if not self._is_running:
                break

            point = Point(
                random.randint(0.2 * Settings.MAP_WIDTH,
                               0.8 * Settings.MAP_WIDTH),
                random.randint(0.2 * Settings.MAP_HEIGHT,
                               0.8 * Settings.MAP_HEIGHT))

            ball = Ball(
                self._score_manager,
                self._obstacle_manager,
                point,
                random.choice(list(Direction)),
                0.1)

            with self._lock:
                self._balls.append(ball)
                ball.run()

    def _run_balls(self):
        for ball in self._balls:
            ball.run()

    def _stop_balls(self):
        with self._lock:
            for ball in self._balls:
                ball.stop()
