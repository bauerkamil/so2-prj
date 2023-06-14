'''
module for Player class
'''
from settings import Settings
from models.obstacle import Obstacle


class Player:
    '''
    class responsible for moving up or down the player on board
    '''

    def __init__(self, obstacle: Obstacle) -> None:
        self._obstacle = obstacle

    @property
    def obstacle(self):
        '''
        returns the obstacle, which is the player
        '''
        return self._obstacle

    def move_down(self):
        '''
        moves the player down if possible
        '''
        first_point, second_point = self._obstacle.points

        first_y = first_point.y
        second_y = second_point.y

        if first_y + 1 > Settings.MAP_HEIGHT or second_y + 1 > Settings.MAP_HEIGHT:
            return

        first_point.set_y(first_point.y + 1)
        second_point.set_y(second_point.y + 1)

    def move_up(self):
        '''
        moves the player up if possible
        '''
        first_point, second_point = self._obstacle.points

        first_y = first_point.y
        second_y = second_point.y

        if first_y - 1 < 0 or second_y - 1 < 0:
            return

        first_point.set_y(first_point.y - 1)
        second_point.set_y(second_point.y - 1)
