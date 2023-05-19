from Settings import Settings
from enums.Direction import Direction
from enums.LineType import LineType
from models.Obstacle import Obstacle
from models.Point import Point
from enums.PlayerNumbers import PlayerNumber


class ObstacleManager:

    def __init__(self, obstacles):
        self._obstacles = obstacles

    @property
    def obstacles_coordinates(self):
        return [tuple([x.points[0].coordinates, x.points[1].coordinates]) for x in self._obstacles]

    def player_got_point(self, x):
        if x == 0:
            return PlayerNumber.ONE

        if x == Settings.MAP_WIDTH:
            return PlayerNumber.TWO

        return None

    def get_direction(self, point: Point, direction: Direction):
        future_point = self._get_future_point(point, direction)

        new_direction = self._check_corners(future_point)
        if new_direction != None:
            return new_direction

        for obstacle in self._obstacles:
            if obstacle.contains_point(future_point):
                return self._get_new_direction(obstacle.line_type, direction)

        return direction

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

        raise Exception("Invalid arguments")
