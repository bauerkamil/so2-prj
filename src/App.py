'''
main module
application's starting point
'''
from settings import Settings
from game import Game
from enums.line_type import LineType
from managers.ball_manager import BallManager
from managers.obstacle_manager import ObstacleManager
from managers.player_manager import PlayerManager
from managers.score_manager import ScoreManager
from models.obstacle import Obstacle
from models.player import Player
from models.point import Point


def initialize():
    '''
    initializes required objects

    returns an object of the Game
    '''
    player_1 = Player(
        Obstacle(
            Point(0, 30),
            Point(0, 30 + Settings.USER_HEIGHT),
            LineType.VERTICAL))
    player_2 = Player(
        Obstacle(
            Point(Settings.MAP_WIDTH, 15),
            Point(Settings.MAP_WIDTH, 15 + Settings.USER_HEIGHT),
            LineType.VERTICAL))
    obstacles = [
        Obstacle(
            Point(0, 0),
            Point(Settings.MAP_WIDTH, 0),
            LineType.HORIZONTAL),
        Obstacle(
            Point(Settings.MAP_WIDTH, Settings.MAP_HEIGHT),
            Point(0, Settings.MAP_HEIGHT),
            LineType.HORIZONTAL),
        player_1.obstacle,
        player_2.obstacle
    ]
    score_manager = ScoreManager()
    obstacle_manager = ObstacleManager(obstacles)
    ball_manager = BallManager(obstacle_manager, score_manager)
    player_manager = PlayerManager(player_1, player_2)

    return Game(obstacle_manager, ball_manager, score_manager, player_manager)


def main():
    '''
    application's main method
    '''

    game = initialize()

    game.play()


if __name__ == "__main__":
    main()
