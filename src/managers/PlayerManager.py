

from enums.PlayerNumbers import PlayerNumber
from models.Player import Player


class PlayerManager:

    def __init__(self, player_1: Player, player_2: Player) -> None:
        self._player_1 = player_1
        self._player_2 = player_2

    def move_up(self, playerNumber: PlayerNumber):
        if (playerNumber == PlayerNumber.ONE):
            self._player_1.move_up()
        else:
            self._player_2.move_up()

    def move_down(self, playerNumber: PlayerNumber):
        if (playerNumber == PlayerNumber.ONE):
            self._player_1.move_down()
        else:
            self._player_2.move_down()
