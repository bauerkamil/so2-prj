import pygame

from pygame.locals import *
from BallManager import BallManager

from ObstacleManager import ObstacleManager
from ScoreManager import ScoreManager
from Settings import Settings


class Game:
    def __init__(self,
                 obstacle_manager: ObstacleManager,
                 ball_manager: BallManager,
                 score_manager: ScoreManager):
        pygame.init()
        pygame.font.init()
        pygame.time.Clock().tick(10)
        pygame.display.set_caption(Settings.TITLE)
        self._font = pygame.font.SysFont('Comic Sans MS', Settings.SCALE * 6)
        self._screen = pygame.display.set_mode(
            (Settings.MAP_WIDTH * Settings.SCALE, Settings.MAP_HEIGHT * Settings.SCALE))
        self._screen.fill(Settings.BACKGROUND_COLOR)
        pygame.display.flip()
        self._obstacle_manager = obstacle_manager
        self._ball_manager = ball_manager
        self._score_manager = score_manager

    def play(self):
        running = True
        self._ball_manager.run()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._ball_manager.stop()
                    running = False

            self._ball_manager.refresh_running_balls()

            self._screen.fill(Settings.BACKGROUND_COLOR)

            for [start, end] in self._obstacle_manager.obstacles_coordinates:
                pygame.draw.line(self._screen, (0, 0, 255),
                                 tuple([x * Settings.SCALE for x in start]),
                                 tuple([x * Settings.SCALE for x in end]), Settings.SCALE)

            for ball_coordinates in self._ball_manager.balls_coordinates:
                pygame.draw.circle(self._screen, (0, 255, 255),
                                   tuple([x * Settings.SCALE for x in ball_coordinates]), Settings.SCALE)

            [first, second] = self._score_manager.score
            font = self._font.render(f'{first} : {second}', False, (0, 0, 0))
            self._screen.blit(
                font, (Settings.SCALE * (Settings.MAP_WIDTH / 2.15), Settings.SCALE * (Settings.MAP_HEIGHT * 0.05)))

            pygame.display.flip()
