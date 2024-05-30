import pygame
from character import Character


class Player(Character):

    def __init__(self, cx, cy, image, border: tuple):
        super().__init__(cx, cy, image, border)

    def get_event(self, **kwargs):

        if kwargs['key_pressed'][pygame.K_LEFT]:
            self.rect.move_ip([-8, 0])
        if kwargs['key_pressed'][pygame.K_RIGHT]:
            self.rect.move_ip([8, 0])
        if kwargs['key_pressed'][pygame.K_UP]:
            self.rect.move_ip([0, -8])
        if kwargs['key_pressed'][pygame.K_DOWN]:
            self.rect.move_ip([0, 8])

    def attack(self):
        pass


class DetectCollision:
    pass
