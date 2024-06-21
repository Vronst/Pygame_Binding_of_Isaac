import pygame
import random

class Item(pygame.sprite.Sprite):

    def __init__(self, cx, cy, image, borders):
        super().__init__()
        self.image = image #sprite image
        self.rect = self.image.get_rect() #rect of the sprite
        self.rect.center = (cx, cy) #start position
        self.borders = borders #borders of the display

    def _move(self, group=None):
        pass

    def update(self, key_pressed=None, group=None, obstacles=None, borders: tuple = (1200, 800)):
        self._move()


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


class PlayerSword(EnemyBullet):

    def __init__(self, cx, cy, image, borders, direction: str, speed=3, range=100, owner=None):
        super().__init__(cx, cy, image, borders, direction, speed)
        self.start = (cx, cy)
        self.cooldown = 2000
        self._last_cooldown = 0
        self.returning = False
        self.range = range
        self.owner = owner

    def _move(self, group=None):
        if not self.returning or not self.owner:
            print('start')
            super()._move()

        if (0 > self.rect.center[0] or self.rect.center[0] > self.borders[0]) or (0 > self.rect.center[1] or self.rect.center[1] > self.borders[1]):
            self.kill()
            
        check1, check2 = self.rect.center[0] - self.start[0], self.rect.center[1] - self.start[1]
        if not self.returning and (check1 < -self.range or check1 > self.range or check2 > self.range or check2 < -self.range):
            self.speed *= -1
            self.returning = True
        if not self.owner:
            if self.returning and self.rect.center == self.start:
                self.kill()
        else:
            distance_x = self.rect.x - self.owner.rect.x
            distance_y = self.rect.y - self.owner.rect.y
            # right
            if self.returning:
                if distance_x > 0:
                    self.rect.move_ip(self.speed, 0)
                # left
                if distance_x < 0:
                    self.rect.move_ip(-self.speed, 0)
                # up
                if distance_y < 0:
                    self.rect.move_ip(0, -self.speed)
                # down
                if distance_y > 0:
                    self.rect.move_ip(0, self.speed)
                if self.returning and self.rect.colliderect(self.owner.rect):
                    print('here')
                    self.kill()
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, surface):
        self._move()
        self.draw(surface)
