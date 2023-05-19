from Settings import Settings
from enums.LineType import LineType
from managers.BallManager import BallManager
from managers.ObstacleManager import ObstacleManager
from managers.PlayerManager import PlayerManager
from managers.ScoreManager import ScoreManager
from Game import Game
from models.Obstacle import Obstacle
from models.Player import Player
from models.Point import Point


def initialize():
    player_1 = Player(Obstacle(Point(0, 30), Point(
        0, 45), LineType.VERTICAL))
    player_2 = Player(Obstacle(Point(Settings.MAP_WIDTH, 15), Point(
        Settings.MAP_WIDTH, 30), LineType.VERTICAL))
    obstacles = [
        Obstacle(Point(0, 0), Point(
            Settings.MAP_WIDTH, 0), LineType.HORIZONTAL),
        Obstacle(Point(Settings.MAP_WIDTH, Settings.MAP_HEIGHT), Point(
            0, Settings.MAP_HEIGHT), LineType.HORIZONTAL),
        player_1.obstacle,
        player_2.obstacle
    ]
    score_manager = ScoreManager()
    obstacle_manager = ObstacleManager(obstacles)
    ball_manager = BallManager(obstacle_manager, score_manager)
    player_manager = PlayerManager(player_1, player_2)

    return Game(obstacle_manager, ball_manager, score_manager, player_manager)


def main():

    game = initialize()

    game.play()


if __name__ == "__main__":
    main()
