import pygame
from character import Character
from item import PlayerSword


class Player(Character):

    def __init__(self, cx, cy, images, border: tuple, obstacles=None, traps=None, weapon=None):
        super().__init__(cx, cy, images[0], border)
        self.traps = traps
        self.obstacles = obstacles
        self.cords = (0, 0)
        self.images = images  # hero animation images list
        self.image_index = 0  # current animation index image
        self.animation_delay = 13  # set animation delay
        self.last_delay = self.animation_delay  # set last delay
        self.health = 100  # starting player health
        self.max_health = 100  # maximum player health
        self.border = border  # border for window dimensions
        self.weapon = weapon  # image of weapon
        self.attacks = pygame.sprite.Group()
        self._lastcooldown = 0
        self.cooldown = 3000

    def check_collision(self, move):
        self.rect.move_ip(move)
        if pygame.sprite.spritecollideany(self, self.obstacles):
            self.rect.move_ip((-move[0], -move[1]))
        if pygame.sprite.spritecollideany(self, self.traps):
            self.take_damage(15)

    def get_event(self, **kwargs):
        # Player moves by 8 pixels when key pressed
        if kwargs['key_pressed'][pygame.K_LEFT]:
            self.check_collision([-8, 0])
        if kwargs['key_pressed'][pygame.K_RIGHT]:
            self.check_collision([8, 0])
        if kwargs['key_pressed'][pygame.K_UP]:
            self.check_collision([0, -8])
        if kwargs['key_pressed'][pygame.K_DOWN]:
            self.check_collision([0, 8])
        if kwargs['key_pressed'][pygame.K_w]:
            self.attack('up')
        if kwargs['key_pressed'][pygame.K_s]:
            self.attack('down')
        if kwargs['key_pressed'][pygame.K_a]:
            self.attack('left')
        if kwargs['key_pressed'][pygame.K_d]:
            self.attack('right')
        self.last_delay -= 1  # decreasing delay
        if self.last_delay <= 0:
            self.image_index += 1  # go to the next animation image
            if self.image_index >= len(self.images):  # setting loop
                self.image_index = 0
            self.image = self.images[self.image_index]  # replace animation image with next index
            self.last_delay = self.animation_delay  # reset delay

    def attack(self, direction=None):
        position = {'up': (self.rect.center[0], self.rect.top), 'down': (self.rect.center[0], self.rect.bottom,),
                        'left': (self.rect.left, self.rect.center[1]), 'right': (self.rect.right, self.rect.center[1])}[direction]
        if not self.attacks.sprites():
            attack = PlayerSword(cx=position[0], cy=position[1], image=self.weapon, borders=self.borders, direction=direction, owner=self)
            self.attacks.add(attack)


    def draw(self, display):
        super().draw(display)
        self.draw_health_bar(display)
        self.attacks.update(display)

    def draw_health_bar(self, display):
        health_bar_width = self.border[0] // 2  # half the window width
        health_bar_height = 20  # health bar height
        health_bar_x = (self.border[0] - health_bar_width) // 2  # health bar centered
        health_bar_y = self.border[1] - health_bar_height - 20  # health bar on bottom

        health_percentage = self.health / self.max_health  # health percentage
        current_health_width = int(health_bar_width * health_percentage)  # actual health

        health_bar_color = (255, 0, 0)  # red is life
        death_color = (0, 0, 0)  # black is death

        pygame.draw.rect(display, death_color, (health_bar_x, health_bar_y, health_bar_width, health_bar_height)) #death bar
        pygame.draw.rect(display, health_bar_color, (health_bar_x, health_bar_y, current_health_width, health_bar_height)) #health bar

    def take_damage(self, amount):  # take damage method, decreasing health level
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):  # increasing health level method
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
