import threading
import logging

# threading.TIMEOUT_MAX = 1

class Score:

    def __init__(self):
        self._player1_score = 0
        self._player1_lock = threading.Lock()

        self._player2_score = 0
        self._player2_lock = threading.Lock()

    @property
    def get_score(self):
        with self._player1_lock:
            with self._player2_lock:
                return (self._player1_score, self._player2_score)
    
    def add_point_player1(self): 
        try:
           with self._player1_lock:
               self._player1_score += 1
        except Exception as e: 
            logging.exception(e)

    def add_point_player2(self):
        try:
           with self._player2_lock:
                self._player2_score += 1
        except Exception as e: 
            logging.exception(e)

    

