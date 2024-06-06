import pygame


class Door(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.rooms = {'top': None, 'bottom': None, 'left': None, 'right': None}
        self.image = image
        self.rect = self.image.get_rect()
