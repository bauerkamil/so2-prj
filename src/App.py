import logging # This module is thread safe.
from Ball import Ball
from Score import Score

logging.basicConfig(level=logging.INFO)



def main():
    score = Score()
    ball1 = Ball(score, 100, 100, 0.5)
    ball2 = Ball(score, 500, 500, 0.3)

    ball1.run()
    ball2.run()

    input()

    ball1.stop()
    ball2.stop()


if __name__ == "__main__":
    main()