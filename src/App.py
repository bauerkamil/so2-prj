from Ball import Ball
from BallManager import BallManager
from ObstacleManager import ObstacleManager
from Point import Point
from ScoreManager import ScoreManager
from Game import Game


def main():
    score_manager = ScoreManager()
    obstacle_manager = ObstacleManager()
    ball_manager = BallManager(obstacle_manager, score_manager)

    game = Game(obstacle_manager, ball_manager, score_manager)
    game.play()


if __name__ == "__main__":
    main()
