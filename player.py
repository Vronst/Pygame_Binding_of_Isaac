import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, image, cx, cy):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = cx, cy
        self.level = None

    def draw(self, surface):
        surface.blit(self.image, self.rect)
