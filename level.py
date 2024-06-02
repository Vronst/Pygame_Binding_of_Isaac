import pygame
from random import randint
from character import Character
from enemies import *


class DetectCollision:

    def __init__(self, player: Character, borders: tuple, images: dict, surface: pygame.Surface, background):
        self.background = background
        self.surface = surface
        self.enemies = {0: (MeleeEnemy, images['PLAYER']), 1: (RangeEnemy, images['PLAYER'])}  # to be more complicated
        self.player = player
        self.set_of_enemies = pygame.sprite.Group()
        self.set_of_obstacles = pygame.sprite.Group()
        self.borders = borders
        # for safety run new_level last in init
        self.new_level()

    def new_level(self):
        for _ in range(randint(0, 4)):
            # shot purpose is to choose melee or range enemy and their image
            shot = randint(0, len(self.enemies) - 1)
            new = (self.enemies[shot][0]
                   (randint(0, self.borders[0]),
                    randint(0, self.borders[1]),
                    self.enemies[shot][1],
                    self.borders,
                    self.player))
            self.set_of_enemies.add(new)  # ignore yellow warning
        self.draw(self.surface)
        # pygame.time.delay(200)

    def update(self):
        self.set_of_enemies.update(group=self.set_of_enemies, obstacles=self.set_of_obstacles)
        self.set_of_obstacles.update()

    def draw(self, screen):
        self.set_of_enemies.draw(screen)

    def pause(self):
        pass
