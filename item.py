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
