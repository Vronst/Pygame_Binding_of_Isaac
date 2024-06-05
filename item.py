import pygame
import random

class Item(pygame.sprite.Sprite):

    def __init__(self, cx, cy, image, borders):
        super().__init__()
        self.image = image #sprite image
        self.rect = self.image.get_rect() #rect of the sprite
        self.rect.center = (cx, cy) #start position
        self.borders = borders #borders of the display

class Heart(Item):

    def __init__(self, image, borders):
        super().__init__(random.randint(0, borders[0]), random.randint(0, borders[1]), image, borders) #random position of heart

    def spawn(self):
        self.rect.center = (random.randint(0, self.borders[0]), random.randint(0, self.borders[1])) #setting new random position  of heart and spawn it on a display

    def heal(self, player):
        player.heal(5)  # +5hp

class EnemyBullet(Item):
    def __init__(self, cx, cy, image, borders: tuple, direction: str, speed=3):
        super().__init__(cx, cy, image, borders)
        self.direction = direction
        self.speed = speed

    def _move(self, group=None):
        if self.direction == 'left':
            self.rect.move_ip((-self.speed, 0))
        elif self.direction == 'right':
            self.rect.move_ip(self.speed, 0)
        elif self.direction == 'up':
            self.rect.move_ip(0, -self.speed)
        elif self.direction == 'down':
            self.rect.move_ip(0, self.speed)

    def update(self, key_pressed=None, group=None, obstacles=None, borders: tuple = (1200, 800)):
        self._move()