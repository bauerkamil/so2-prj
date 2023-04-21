import logging # This module is thread safe.
from Ball import Ball
from Board import Board
from Point import Point
from Score import Score

logging.basicConfig(level=logging.INFO)



def main():
    score = Score()
    board = Board(200, 100)
    ball1 = Ball(score, board, Point(100, 90), 0.2)
    ball2 = Ball(score, board, Point(87, 57), 0.1)
    ball3 = Ball(score, board, Point(140, 86), 0.1)

    ball1.run()
    ball2.run()
    ball3.run()

    input()

    ball1.stop()
    ball2.stop()
    ball3.stop()


if __name__ == "__main__":
    main()