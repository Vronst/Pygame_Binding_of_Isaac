from character import Character
from random import randint
import pygame


class Enemy(Character):
    def __init__(self, cx, cy, image, borders, player, move_x=5, move_y=5):
        super().__init__(cx, cy, image, borders)
        self.player = player.rect
        self.move_x = move_x
        self.move_y = move_y
        self._moves = ((self.move_x, 0), (-self.move_x, 0), (0, self.move_y), (0, -self.move_y))
        self.melee = True

    def set_moves(self, x, y):
        self._moves = ((x, 0), (-x, 0), (0, y), (0, -y))

    def _move(self, group=None):
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

    def __init__(self, cx, cy, image, borders, player, move_x=5, move_y=5):
        super().__init__(cx, cy, image, borders, player, move_x, move_y)

    def tired(self):
        pass


class RangeEnemy(Enemy):
    def __init__(self, cx, cy, image, borders, player, move_x=-3, move_y=5):
        super().__init__(cx, cy, image, borders, player, move_x, move_y)
        self.melee = False

    def attack(self):
        pass


class DetectCollision:

    def __init__(self, player: Character, borders: tuple, images: dict, surface: pygame.Surface, background):
        self.background = background
        self.surface = surface
        self.enemies = {0: (MeleeEnemy, images['PLAYER']), 1: (RangeEnemy, images['PLAYER'])}  # to be more complicated
        self.player = player
        self.set_of_enemies = pygame.sprite.Group()
        self.set_of_obstacle = pygame.sprite.Group()
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
            if (not pygame.sprite.spritecollideany(new, self.set_of_enemies)
                    and not pygame.sprite.spritecollideany(new, self.set_of_obstacle)):
                self.set_of_enemies.add(new)  # ignore yellow warning
        self.draw(self.surface)

    def update(self):
        self.set_of_enemies.update()
        self.set_of_obstacle.update()

    def draw(self, screen):
        self.set_of_enemies.draw(screen)

    def pause(self):
        pass
