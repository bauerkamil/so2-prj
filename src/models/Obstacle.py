'''
module for Obstacle class
'''
from enums.line_type import LineType
from models.point import Point


class Obstacle:
    '''
    class responsible for storing data about obstacle and it's:
        start_point
        end_point
        line_type
    '''

    def __init__(self, first_point: Point, second_point: Point, line_type: LineType) -> None:

        self._line_type = line_type

        first_x, first_y = first_point.coordinates
        second_x, second_y = second_point.coordinates

        match line_type:
            case LineType.VERTICAL:
                if first_x != second_x:
                    raise ValueError("invalid vertical line")
                if first_y < second_y:
                    self._start_point = first_point
                    self._end_point = second_point
                else:
                    self._start_point = second_point
                    self._end_point = first_point
            case LineType.HORIZONTAL:
                if first_y != second_y:
                    raise ValueError("invalid horizontal line")
                if first_x < second_x:
                    self._start_point = first_point
                    self._end_point = second_point
                else:
                    self._start_point = second_point
                    self._end_point = first_point
            case _:
                raise ValueError("invalid line type")

    def contains_point(self, point: Point):
        '''
        returns true if the point is within the obstacle
        '''
        point_x, point_y = point.coordinates

        start_x, start_y = self._start_point.coordinates
        end_x, end_y = self._end_point.coordinates

        match self._line_type:
            case LineType.HORIZONTAL:
                if point_y == start_y and point_x >= start_x and point_x <= end_x:
                    return True
            case LineType.VERTICAL:
                if point_x == start_x and point_y >= start_y and point_y <= end_y:
                    return True
            case _:
                raise ValueError("invalid line type")
        return False

    @property
    def line_type(self):
        '''
        returns the line type
        '''
        return self._line_type

    @property
    def points(self):
        '''
        returns tuple(start_point, end_point)
        '''
        return self._start_point, self._end_point
