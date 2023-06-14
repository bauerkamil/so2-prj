'''
module for Game class
'''
import pygame

from pygame.locals import *

from enums.player_numbers import PlayerNumber
from managers.ball_manager import BallManager
from managers.obstacle_manager import ObstacleManager
from managers.player_manager import PlayerManager
from managers.score_manager import ScoreManager
from settings import Settings


class Game:
    '''
    class responsible for joining pygame with logic of the game
    '''

    def __init__(self,
                 obstacle_manager: ObstacleManager,
                 ball_manager: BallManager,
                 score_manager: ScoreManager,
                 player_manager: PlayerManager):

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
        self._player_manager = player_manager

    def play(self):
        '''
        starts the game
        '''
        running = True
        self._ball_manager.run()
        self._obstacle_manager.run()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._ball_manager.stop()
                    self._obstacle_manager.stop()
                    running = False
                self._handle_key_event(event)

            self._ball_manager.refresh_running_balls()

            self._screen.fill(Settings.BACKGROUND_COLOR)

            self._draw_obstacles()
            self._draw_balls()
            self._draw_score()

            pygame.display.flip()

    def _handle_key_event(self, event):
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_w:
                    self._player_manager.move_up(PlayerNumber.ONE)

                case pygame.K_s:
                    self._player_manager.move_down(PlayerNumber.ONE)

                case pygame.K_UP:
                    self._player_manager.move_up(PlayerNumber.TWO)

                case pygame.K_DOWN:
                    self._player_manager.move_down(PlayerNumber.TWO)

    def _draw_obstacles(self):
        for [start, end] in self._obstacle_manager.obstacles_coordinates:
            pygame.draw.line(
                self._screen,
                (0, 0, 255),
                tuple([x * Settings.SCALE for x in start]),
                tuple([x * Settings.SCALE for x in end]),
                Settings.SCALE)

    def _draw_balls(self):
        for ball_coordinates in self._ball_manager.balls_coordinates:
            pygame.draw.circle(
                self._screen,
                (0, 255, 255),
                tuple([x * Settings.SCALE for x in ball_coordinates]),
                Settings.SCALE)

    def _draw_score(self):
        [first, second] = self._score_manager.score
        font = self._font.render(f'{second} : {first}', False, (0, 0, 0))
        self._screen.blit(
            font,
            (Settings.SCALE * (Settings.MAP_WIDTH / 2.15),
             Settings.SCALE * (Settings.MAP_HEIGHT * 0.05)))
