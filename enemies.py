import pygame
import os
from character import Character
from item import EnemyBullet
from time import time


class Enemy(Character):
    def __init__(self, cx, cy, image, borders, player, move_x, move_y, obstacles=None, health=3):
        super().__init__(cx, cy, image, borders, obstacles)
        self.player = player
        self.move_x = move_x
        self.move_y = move_y
        self._moves = ((self.move_x, 0), (-self.move_x, 0), (0, self.move_y), (0, -self.move_y))
        self._melee = True
        self.attacks = pygame.sprite.Group()
        self.cooldown = 2000  # cooldown time - now 2 seconds
        self._last_cooldown = pygame.time.get_ticks()
        self.health = health
        self.immunity_time = 1
        self.damaged_time = time()
        self.time = time()

    # not used thus commented
    # def set_moves(self, x, y):
    #     self._moves = ((x, 0), (-x, 0), (0, y), (0, -y))  # how much object will move per update

    def _move(self, group=None):
        self.time = time()
        # colliding with players attacks
        if pygame.sprite.spritecollideany(self, self.player.attacks) and self.time - self.damaged_time > self.immunity_time:
            print(self.health, time())
            self.damaged_time = time()
            self.health -= 1
            if self.health == 0:
                self.kill()

        # making it move dependent of player object
        distance_x = self.rect.x - self.player.rect.x
        distance_y = self.rect.y - self.player.rect.y
        if distance_x < 0:
            direction = 'right'
        elif distance_x > 0:
            direction = 'left'
        elif distance_y > 0:
            direction = 'up'
        else:
            direction = 'down'
        temp = self.attack(direction)
        if temp:
            self.attacks.add(temp)

        if group:
            group = [x for x in group if x != self]
        moves = []
        # go right if melee (else left, init of range enemy inverts x)
        if distance_x < 0:
            moves.append(self._moves[0])
        # go left if melee (else right)
        if distance_x >= 0:
            moves.append(self._moves[1])
        # down
        if distance_y < 0:
            moves.append(self._moves[2])
        # up
        if distance_y > 0:
            moves.append(self._moves[3])

        for move in moves:
            if not self.tired():
                self.rect.move_ip(move)
                if self.obstacles and pygame.sprite.spritecollideany(self, self.obstacles):
                    self.rect.move_ip(-move[0], -move[1])
            for member in group:
                if self.rect.colliderect(member):
                    self.rect.move_ip(-move[0], -move[1])


    def attack(self, direction: str = 'down'):
        pass

    # not used but still here
    def is_melee(self):
        return self._melee


class MeleeEnemy(Enemy):

    def __init__(self, cx, cy, image, borders, player, move_x=4, move_y=4, obstacles=None):
        super().__init__(cx, cy, image, borders, player, move_x, move_y, obstacles)
        self.cooldown = 4000
        self._rest = 0

    def tired(self) -> bool:
        now = pygame.time.get_ticks()  # getting relative variable
        if now - self._last_cooldown > self.cooldown:  # checking the difference
            if now - self._rest > self.cooldown:  # this one ensures that Object will rest
                self._last_cooldown = now  # this and self.rest - reset cycle
            return False
        else:
            self._rest = now
            return True


class RangeEnemy(Enemy):
    def __init__(self, cx, cy, image, borders, player, move_x=3, move_y=5, obstacles=None):
        super().__init__(cx, cy, image, borders, player, -move_x, move_y, obstacles)
        self._melee = False
        self.limit[0] = 100

    def attack(self, direction: str = 'down'):
        now = pygame.time.get_ticks()
        if now - self._last_cooldown > self.cooldown:
            path = os.path.join(os.getcwd(), 'images')
            if self.rect.x < self.player.rect.x:  # player on the right side
                bullet_image = pygame.image.load(os.path.join(path, 'bullet_right.png')).convert_alpha()
            else:  # player on the left side
                bullet_image = pygame.image.load(os.path.join(path, 'bullet_left.png')).convert_alpha()

            bullet = EnemyBullet(self.rect.x, self.rect.y, bullet_image, self.borders, direction, 3)
            self._last_cooldown = now
            return bullet
