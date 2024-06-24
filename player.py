import pygame
from character import Character
from item import PlayerSword
from time import time

class Player(Character):

    def __init__(self, cx, cy, images, border: tuple, obstacles=None, traps=None, weapon=None):
        super().__init__(cx, cy, images['idle'][0], border, obstacles)
        self.traps = traps
        self.cords = (0, 0)
        self.images = images  # hero animation images list
        self.current_images = self.images['idle']  # well...
        self.health = 100  # starting player health
        self.max_health = 100  # maximum player health
        self.weapon = weapon  # image of weapon
        self.attacks = pygame.sprite.Group()
        self._lastcooldown = 0
        self.cooldown = 3000
        self.is_attacking = False #tracking if player is attacking
        self.attack_direction = None #tracking the attack direction
        self.items = []  # for players items - only works with 'force' now
        self.range = 200  # could be eddited by items

    def check_collision(self, move):
        self.rect.move_ip(move)
        if pygame.sprite.spritecollideany(self, self.obstacles):
            self.rect.move_ip((-move[0], -move[1]))
        if pygame.sprite.spritecollideany(self, self.traps):
            self.take_damage(15)

    def _get_event(self, **kwargs):
        # Player moves by 6 pixels when key pressed
        key_pressed = kwargs['key_pressed']
        if key_pressed[pygame.K_UP]:
            self.check_collision([0, -6])
            self.current_images = self.images['up']  #switch to up movement images
        if key_pressed[pygame.K_DOWN]:
            self.check_collision([0, 6])
            self.current_images = self.images['down']  #switch to down movement images
        if key_pressed[pygame.K_LEFT]:
            self.check_collision([-6, 0])
            self.current_images = self.images['left']  #switch to left movement images
        if key_pressed[pygame.K_RIGHT]:
            self.check_collision([6, 0])
            self.current_images = self.images['right']  #switch to right movement images
        if not any(key_pressed):
            self.current_images = self.images['idle']  #switch back to idle images

        if kwargs['key_pressed'][pygame.K_w]:
            self.current_images = self.images['attack_up']  #switch to up attack images
            self.attack('up')
        if kwargs['key_pressed'][pygame.K_s]:
            self.current_images = self.images['attack_down']  #switch to down attack images
            self.attack('down')
        if kwargs['key_pressed'][pygame.K_a]:
            self.current_images = self.images['attack_left']  #switch to left attack images
            self.attack('left')
        if kwargs['key_pressed'][pygame.K_d]:
            self.current_images = self.images['attack_right']  #switch to right attack images
            self.attack('right')

        self.last_delay -= 1  # decreasing delay
        if self.last_delay <= 0:
            self.image_index += 1  # go to the next animation image
            if self.image_index >= len(self.current_images):  # setting loop
                self.image_index = 0
                self.current_images = self.images['idle']
            self.image = self.current_images[self.image_index]  # replace animation image with next index
            self.last_delay = self.animation_delay  # reset delay

    def attack(self, direction=None):
        position = {'up': (self.rect.center[0], self.rect.top),
                    'down': (self.rect.center[0], self.rect.bottom),
                    'left': (self.rect.left, self.rect.center[1]),
                    'right': (self.rect.right, self.rect.center[1])
                    }[direction]

        rotation = {'up': 90, 'down': -90, 'left': 180, 'right': 0}[direction]

        # change to - and not self.attacks.sprites() - if u want it to be single ranged strike
        if self.weapon and len(self.attacks.sprites()) <=2 and self.image_index == len(self.current_images) - 3:
            rotated_weapon = pygame.transform.rotate(self.weapon, rotation)
            attack = PlayerSword(cx=position[0], cy=position[1], image=rotated_weapon, borders=self.borders, direction=direction, owner=self)
            self.attacks.add(attack)
            if 'force' in self.items and len(self.attacks.sprites()) <=1:
                attack = PlayerSword(cx=position[0], cy=position[1], image=rotated_weapon, 
                                     borders=self.borders, direction=direction, owner=self,
                                     range=self.range)
                attack.ranged = True
                self.attacks.add(attack)



    def draw(self, display):
        super().draw(display)
        self.draw_health_bar(display)
        self.attacks.update(display)

    def draw_health_bar(self, display):
        health_bar_width = self.borders[0] // 2  # half the window width
        health_bar_height = 20  # health bar height
        health_bar_x = (self.borders[0] - health_bar_width) // 2  # health bar centered
        health_bar_y = self.borders[1] - health_bar_height - 20  # health bar on bottom

        health_percentage = self.health / self.max_health  # health percentage
        current_health_width = int(health_bar_width * health_percentage)  # actual health

        health_bar_color = (255, 0, 0)  # red is life
        death_color = (0, 0, 0)  # black is death

        pygame.draw.rect(display, death_color, (health_bar_x, health_bar_y, health_bar_width, health_bar_height)) #death bar
        pygame.draw.rect(display, health_bar_color, (health_bar_x, health_bar_y, current_health_width, health_bar_height)) #health bar

    def take_damage(self, amount):  # take damage method, decreasing health level
        if not self.immune():
            self.health -= amount
            if self.health < 0:
                self.health = 0
            self.damaged_time = time()

    def heal(self, amount):  # increasing health level method
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
