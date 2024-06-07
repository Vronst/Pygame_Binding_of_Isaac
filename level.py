from random import randint
from enemies import *


class DetectCollision:

    def __init__(self,
                 player: Character, borders: tuple, images: dict, surface: pygame.Surface, background, doors=None):
        self.doors = doors
        self.buffs = pygame.sprite.Group()
        self.difficulty = 3
        self.background = background
        self.surface = surface
        self.enemies = {0: (MeleeEnemy, images['MELEE_ENEMY']), 1: (RangeEnemy, images['RANGE_ENEMY'])}
        # to be more complicated
        self.player = player
        self.set_of_enemies = pygame.sprite.Group()
        self.set_of_obstacles = pygame.sprite.Group()
        self.borders = borders
        self.last_damage_time = 0
        # for safety run new_level last in init
        self.new_level()

    def new_level(self):
        for _ in range(randint(0, self.difficulty)):
            # shot purpose is to choose melee or range enemy and their image
            shot = randint(0, len(self.enemies) - 1)
            new = (self.enemies[shot][0]
                   (randint(0, self.borders[0]),
                    randint(0, self.borders[1]),
                    self.enemies[shot][1],
                    self.borders,
                    self.player))
            self.set_of_enemies.add(new)  # ignore yellow warning
        self.draw(self.surface)
        # pygame.time.delay(200)

    def update(self):
        self.buffs.update()
        self.set_of_enemies.update(group=self.set_of_enemies, obstacles=self.set_of_obstacles)

        enemy_bullets_group = pygame.sprite.Group() #group of enemy bullets

        for enemy in self.set_of_enemies:
            for attack in enemy.attacks:
                attack.update()
                enemy_bullets_group.add(attack)  #adding every bullet to enemy bullets group

        self.draw(self.surface)
        enemy_bullets_group.draw(self.surface) #drawing enemy bullets

        collided_bullets = pygame.sprite.spritecollide(self.player, enemy_bullets_group, True) #check collision between player and enemy bullet
        for _ in collided_bullets:
            self.player.take_damage(3)  #deal 3 damage to player

        self.bad_touch() #taking damage by colliding with enemy
        self.set_of_obstacles.update()
        if self.player.health == 0:
            self.restart()

    def draw(self, screen):
        if self.doors:
            self.doors.draw(screen)
        self.buffs.draw(screen)
        self.set_of_enemies.draw(screen)
        self.set_of_obstacles.draw(screen)

    def pause(self):
        pass

    def bad_touch(self):  # taking damage by touching an enemy
        current_time = pygame.time.get_ticks()
        collided_enemy = pygame.sprite.spritecollideany(self.player, self.set_of_enemies)
        if pygame.sprite.spritecollideany(self.player, self.set_of_enemies):
            if current_time - self.last_damage_time >= 1000:  # interval between last taking damage
                self.player.take_damage(2)  # -2hp
                self.last_damage_time = current_time  # reset damage timer
            self.set_of_enemies.remove(collided_enemy)  # remove collided enemy

    def restart(self):
        self.player.health = 100
        self.buffs.empty()
        self.set_of_enemies.empty()
        self.set_of_obstacles.empty()
        self.new_level()

