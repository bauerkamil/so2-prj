'''
module for ScoreManager class
'''
import threading
from enums.player_numbers import PlayerNumber


class ScoreManager:
    '''
    class responsible for storing score and adding points
    '''

    def __init__(self):
        self._player1_score = 0
        self._player1_lock = threading.Lock()

        self._player2_score = 0
        self._player2_lock = threading.Lock()

    @property
    def score(self):
        '''
        returns a score - tuple(player1_score, _player2_score)
        '''
        with self._player1_lock:
            with self._player2_lock:
                return self._player1_score, self._player2_score

    def add_point(self, player: PlayerNumber):
        '''
        adds point to given player
        '''
        if player == PlayerNumber.ONE:
            with self._player1_lock:
                self._player1_score += 1
        else:
            with self._player2_lock:
                self._player2_score += 1


# with some_lock:
#     # do something...

# is equivalent to:

# some_lock.acquire()
# try:
#     # do something...
# finally:
#     some_lock.release()
