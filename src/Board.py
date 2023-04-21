from enums.Direction import Direction
from enums.LineType import LineType
from Obstacle import Obstacle
from Point import Point
from enums.Players import Player

class Board:

    def __init__(self, size_x, size_y):
        self._size_x = size_x
        self._size_y = size_y
        self._obstacles = [
            Obstacle(Point(0, 0), Point(size_x, 0), LineType.HORIZONTAL),
            Obstacle(Point(size_x, size_y), Point(0, size_y), LineType.HORIZONTAL),
        ]

    def player_got_point(self, x):
        if x < 0:
            return Player.ONE
        
        if x > self._size_x:
            return Player.TWO
        
        return None
    
    def get_direction(self, point: Point, direction: Direction):
        new_direction = self._check_corners(point)
        if new_direction != None:
            return new_direction
        
        for obstacle in self._obstacles:
            if obstacle.contains_point(point):
                return self._get_new_direction(obstacle.line_type, direction)
            
        return direction

    def _check_corners(self, point: Point):
        point_x, point_y = point.coordinates
        
        if point_x == 0 and point_y == 0:
            return Direction.UP_RIGHT
        if point_x == 0 and point_y == self._size_y:
            return Direction.DOWN_RIGHT
        if point_x == self._size_x and point_y == 0:
            return Direction.UP_LEFT
        if point_x == self._size_x and point_y == self._size_y:
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

