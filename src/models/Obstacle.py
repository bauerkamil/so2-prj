from enums.LineType import LineType
from models.Point import Point


class Obstacle:

    def __init__(self, first_point: Point, second_point: Point, line_type: LineType) -> None:

        self._line_type = line_type

        first_x, first_y = first_point.coordinates
        second_x, second_y = second_point.coordinates

        match line_type:
            case LineType.VERTICAL:
                if first_x != second_x:
                    raise Exception("invalid vertical line")
                if first_y < second_y:
                    self._start_point = first_point
                    self._end_point = second_point
                else:
                    self._start_point = second_point
                    self._end_point = first_point
            case LineType.HORIZONTAL:
                if first_y != second_y:
                    raise Exception("invalid horizontal line")
                if first_x < second_x:
                    self._start_point = first_point
                    self._end_point = second_point
                else:
                    self._start_point = second_point
                    self._end_point = first_point

    def contains_point(self, point: Point):
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
        return False

    @property
    def line_type(self):
        return self._line_type

    @property
    def points(self):
        return self._start_point, self._end_point
