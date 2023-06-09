'''
module for ObstacleManager class
'''
from random import randrange, choice
from threading import Lock, Thread
from time import sleep
from typing import List
from settings import Settings
from enums.direction import Direction
from enums.line_type import LineType
from models.obstacle import Obstacle
from models.point import Point


class ObstacleManager:
    '''
    class responsible for storing and generating new obstacles
    '''

    def __init__(self, obstacles: List[Obstacle]):
        self._obstacles = obstacles
        self._time_delay = Settings.OBSTACLE_SPAWN_TIME
        self._is_running = False
        self._thread = Thread(target=self._generate_obstacles)
        self._lock = Lock()

    @property
    def obstacles_coordinates(self):
        '''
        returns an array of tuples containing coordinates for obstacles
        '''
        with self._lock:
            return [
                tuple(
                    [x.points[0].coordinates, x.points[1].coordinates]
                ) for x in self._obstacles
            ]

    def get_direction(self, current_point: Point, direction: Direction):
        '''
        returns direction in which the ball should move
        '''
        future_point = self._get_future_point(current_point, direction)

        new_direction = self._check_corners(future_point)
        if new_direction is not None:
            return new_direction

        for obstacle in self._obstacles:
            if obstacle.contains_point(future_point):
                return self._get_new_direction(obstacle.line_type, direction)

        return direction

    def run(self):
        '''
        runs the thread, which generates obstacles
        '''
        self._is_running = True
        self._thread.start()

    def stop(self):
        '''
        stops the thread, which generates obstacles
        '''
        self._is_running = False

    def _get_future_point(self, point: Point, direction: Direction):

        match direction:
            case Direction.UP_RIGHT:
                return Point(point.x + 1, point.y + 1)
            case Direction.UP_LEFT:
                return Point(point.x - 1, point.y + 1)
            case Direction.DOWN_RIGHT:
                return Point(point.x + 1, point.y - 1)
            case Direction.DOWN_LEFT:
                return Point(point.x - 1, point.y - 1)
            case _:
                raise ValueError("invalid direction")

    def _check_corners(self, point: Point):
        point_x, point_y = point.coordinates

        if point_x == 0 and point_y == 0:
            return Direction.UP_RIGHT
        if point_x == 0 and point_y == Settings.MAP_HEIGHT:
            return Direction.DOWN_RIGHT
        if point_x == Settings.MAP_WIDTH and point_y == 0:
            return Direction.UP_LEFT
        if point_x == Settings.MAP_WIDTH and point_y == Settings.MAP_HEIGHT:
            return Direction.DOWN_LEFT

        return None

    def _get_new_direction(self, line_type: LineType, old_direction: Direction):
        if line_type == LineType.HORIZONTAL:
            match old_direction:
                case Direction.UP_LEFT:
                    return Direction.DOWN_LEFT
                case Direction.UP_RIGHT:
                    return Direction.DOWN_RIGHT
                case Direction.DOWN_LEFT:
                    return Direction.UP_LEFT
                case Direction.DOWN_RIGHT:
                    return Direction.UP_RIGHT
                case _:
                    raise ValueError("invalid direction")

        if line_type == LineType.VERTICAL:
            match old_direction:
                case Direction.UP_LEFT:
                    return Direction.UP_RIGHT
                case Direction.UP_RIGHT:
                    return Direction.UP_LEFT
                case Direction.DOWN_LEFT:
                    return Direction.DOWN_RIGHT
                case Direction.DOWN_RIGHT:
                    return Direction.DOWN_LEFT
                case _:
                    raise ValueError("invalid direction")

        raise ValueError("Invalid arguments")

    def _generate_obstacles(self):

        while self._is_running:
            time = 0
            while time < self._time_delay:
                sleep(0.1)
                time += 0.1
                if not self._is_running:
                    break

            point_x = randrange(1, Settings.MAP_WIDTH - 1)
            point_y = randrange(1, Settings.MAP_HEIGHT - 1)
            line_type = choice(list(LineType))

            if line_type == LineType.VERTICAL:
                if point_y + Settings.OBSTACLE_HEIGHT > Settings.MAP_HEIGHT:
                    new_obstacle = Obstacle(
                        Point(point_x, point_y),
                        Point(point_x, point_y-Settings.OBSTACLE_HEIGHT),
                        LineType.VERTICAL)
                else:
                    new_obstacle = Obstacle(
                        Point(point_x, point_y),
                        Point(point_x, point_y+Settings.OBSTACLE_HEIGHT),
                        LineType.VERTICAL)
            else:
                if point_x + Settings.OBSTACLE_HEIGHT > Settings.MAP_WIDTH:
                    new_obstacle = Obstacle(
                        Point(point_x, point_y),
                        Point(point_x - Settings.OBSTACLE_HEIGHT, point_y),
                        LineType.HORIZONTAL)
                else:
                    new_obstacle = Obstacle(
                        Point(point_x, point_y),
                        Point(point_x + Settings.OBSTACLE_HEIGHT, point_y),
                        LineType.HORIZONTAL)

            with self._lock:
                self._obstacles.append(new_obstacle)
