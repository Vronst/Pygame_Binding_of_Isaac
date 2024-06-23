import pygame
from time import time


class Character(pygame.sprite.Sprite):

    def __init__(self, cx, cy, image, borders: tuple = (1200, 800), obstacles=None):
        super().__init__()
        self.obstacles = obstacles
        self.image = image
        # rect represents out character, and save its position
        self.rect = self.image.get_rect()
        self.rect.center = (cx, cy)
        self.borders = borders
        self.limit = [85, 50]  # limit how close to the border it can be
        self.hit = time()
        self.immunity_time = 1.0
        self.damaged_time = time()
        self.time = time()
        self.flash_timer = 0
        self.visible = True
        self.moving = True  # check if object is moving, used for animation
        self.animation_delay = 10  # set animation delay
        self.last_delay = self.animation_delay  # set last delay
        self.image_index = 0  # current animation index image


    def _move(self, group):
        # idea of group here is to have group of object that u can collide with
        pass

    def _get_event(self, **kwargs):
        pass
    
    def immune(self) -> bool:
        if self.time - self.damaged_time > self.immunity_time:
            return False
        else:
            self.time = time()
            return True

    def draw(self, display):
        self.flash_timer += pygame.time.get_ticks()  # TODO: change it to time
        if self.flash_timer >= 10000:
            self.flash_timer = 0
            self.visible = not self.visible
        if self.visible or not self.immune():
            display.blit(self.image, self.rect)


    def update(self, key_pressed=None, group=None):
        # forwarding pressed keys
        self._get_event(key_pressed=key_pressed)
        self._move(group)

        # blocking out of border movement

        # bottom
        if self.rect.bottom > self.borders[1] - self.limit[1]:
            self.rect.bottom = self.borders[1] - self.limit[1]
            self.moving = False
        # top
        if self.rect.top < self.limit[1]:
            self.rect.top = self.limit[1]
            self.moving = False
        # left
        if self.rect.centerx < self.limit[0]:
            self.rect.centerx = self.limit[0]
            self.moving = False
        # right
        if self.rect.centerx > self.borders[0] - self.limit[0]:
            self.rect.centerx = self.borders[0] - self.limit[0]
            self.moving = False

    def tired(self):
        return False
