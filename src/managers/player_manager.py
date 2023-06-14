'''
module for PlayerManager class
'''
from enums.player_numbers import PlayerNumber
from models.player import Player


class PlayerManager:
    '''
    class responsible for communication with Player objects
    '''

    def __init__(self, player_1: Player, player_2: Player) -> None:
        self._player_1 = player_1
        self._player_2 = player_2

    def move_up(self, player_number: PlayerNumber):
        '''
        updates the position of given player
        '''
        if player_number == PlayerNumber.ONE:
            self._player_1.move_up()
        else:
            self._player_2.move_up()

    def move_down(self, player_number: PlayerNumber):
        '''
        updates the position of given player
        '''
        if player_number == PlayerNumber.ONE:
            self._player_1.move_down()
        else:
            self._player_2.move_down()
