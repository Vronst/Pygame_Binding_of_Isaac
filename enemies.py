from character import Character
from random import randint
import pygame


class Enemy(Character):
    def __init__(self, cx, cy, image, borders, player):
        super().__init__(cx, cy, image, borders)
        self.player = player.rect
        self.move_x = 5
        self.move_y = 5
        self._moves = ((self.move_x, 0), (-self.move_x, 0), (0, self.move_y), (0, -self.move_y))
        self.melee = True

    def set_moves(self):
        self._moves = ((self.move_x, 0), (-self.move_x, 0), (0, self.move_y), (0, -self.move_y))

    def _move(self):
        # making it move dependent of player object
        distance_x = self.rect.x - self.player.x
        distance_y = self.rect.y - self.player.y

        if distance_x < 0 or (distance_x >= 0 and self.rect.x > self.borders[0] - 100 and not self.melee):
            self.rect.move_ip(self._moves[0])
        if (distance_x > 0 or
                (distance_x >= 0 and self.rect.x < self.borders[0] - self.borders[0] + 100 and not self.melee)):
            self.rect.move_ip(self._moves[1])
        if distance_y < 0:
            self.rect.move_ip(self._moves[2])
        if distance_y > 0:
            self.rect.move_ip(self._moves[3])


class MeleeEnemy(Enemy):

    def __init__(self, cx, cy, image, borders, player):
        super().__init__(cx, cy, image, borders, player)


class RangeEnemy(Enemy):
    def __init__(self, cx, cy, image, borders, player):
        super().__init__(cx, cy, image, borders, player)
        self.move_x = -3
        self.move_y = 6
        self.set_moves()
        self.melee = False


class DetectCollision:

    def __init__(self, player: Character, borders: tuple):
        self.enemies = {0: MeleeEnemy, 1: 'rangeEnemy'}
        self.player = player
        self.set_of_enemies = pygame.sprite.Group()
        self.set_of_obstacle = pygame.sprite.Group()
        self.borders = borders
        self.images = {0: 'imageMelee', 1: 'image'}
        # for safety run new_level last in init
        self.new_level()

    def new_level(self):
        for _ in range(randint(0, 4)):
            # shot purpose is to choose melee or range enemy and their image
            shot = randint(0, len(self.enemies) - 1)
            new = (self.enemies[shot]
                   (randint(0, self.borders[0]),
                    randint(0, self.borders[1]),
                    self.images[shot],
                    self.borders,
                    self.player))
            if (not pygame.sprite.spritecollideany(new, self.set_of_enemies)
                    and not pygame.sprite.spritecollideany(new, self.set_of_obstacle)
                    and not pygame.sprite.spritecollideany(new, self.player)):  # ignore yellow warning
                self.set_of_enemies.add(new)  # ignore yellow warning

    def update(self):
        pass

    def draw(self, screen):
        pass

    def pause(self):
        pass
