from Settings import Settings
from models.Obstacle import Obstacle


class Player:

    def __init__(self, obstacle: Obstacle) -> None:
        self._obstacle = obstacle

    @property
    def obstacle(self):
        return self._obstacle

    def move_down(self):
        first_point, second_point = self._obstacle.points

        first_y = first_point.y
        second_y = second_point.y

        if (first_y + 1 > Settings.MAP_HEIGHT or second_y + 1 > Settings.MAP_HEIGHT):
            return

        first_point.set_y(first_point.y + 1)
        second_point.set_y(second_point.y + 1)

    def move_up(self):
        first_point, second_point = self._obstacle.points

        first_y = first_point.y
        second_y = second_point.y

        if (first_y - 1 < 0 or second_y - 1 < 0):
            return

        first_point.set_y(first_point.y - 1)
        second_point.set_y(second_point.y - 1)
