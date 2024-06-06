import pygame


class Character(pygame.sprite.Sprite):

    def __init__(self, cx, cy, image, borders: tuple = (1200, 800)):
        super().__init__()
        self.image = image
        # rect represents out character, and save its position
        self.rect = self.image.get_rect()
        self.rect.center = (cx, cy)
        self.borders = borders

    def _move(self, group):
        pass

    def get_event(self, **kwargs):
        pass

    def draw(self, display):
        display.blit(self.image, self.rect)

    def update(self, key_pressed=None, group=None, obstacles=None):
        self.get_event(key_pressed=key_pressed)
        self._move(group)

        # blocking out of border movement
        # bottom
        if self.rect.bottom > self.borders[1] - 50:
            self.rect.bottom = self.borders[1] - 50
        # top
        if self.rect.top < 50:
            self.rect.top = 50
        # left
        if self.rect.centerx < 100:
            self.rect.centerx = 100
        # right
        if self.rect.centerx > self.borders[0] - 85:
            self.rect.centerx = self.borders[0] - 85

    def tired(self):
        return False
