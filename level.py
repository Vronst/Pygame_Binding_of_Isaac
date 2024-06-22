from random import randint, choices
from enemies import *


class Level:

    def __init__(self,
                 player, borders: tuple, images: dict, surface: pygame.Surface,
                 background, doors=None, first=None):
        self.images = images
        self.obstacle_gen = Obstacles(borders)
        self.doors = doors
        self.buffs = pygame.sprite.Group()
        self.difficulty = 3
        self.background = background
        self.surface = surface
        self.enemies = {0: (MeleeEnemy, self.images['MELEE_ENEMY']), 1: (RangeEnemy, self.images['RANGE_ENEMY'])}
        self.player = player
        self.set_of_enemies = pygame.sprite.Group()
        self.borders = borders
        self.last_damage_time = 0
        # for safety run new_level last in init
        self.new_level(first)

    def new_level(self, first=None) -> None:
        if not first:
            self.obstacle_gen.random_gen(self.images['CRYSTAL_OBSTACLE'])
            for _ in range(randint(0, self.difficulty)):
                # shot purpose is to choose melee or range enemy and their image
                shot = randint(0, len(self.enemies) - 1)
                new = (self.enemies[shot][0]
                       (randint(0, self.borders[0]),
                        randint(0, self.borders[1]),
                        self.enemies[shot][1],
                        self.borders,
                        self.player, obstacles=self.obstacle_gen.obstacles))
                self.set_of_enemies.add(new)

        self.draw(self.surface)

    def update(self) -> None:
        self.player.obstacles = self.obstacle_gen.obstacles
        self.player.traps = self.obstacle_gen.traps
        self.buffs.update()
        self.set_of_enemies.update(group=self.set_of_enemies)  # need to past it so it know where is everybody and who collided with who

        enemy_bullets_group = pygame.sprite.Group()  # group of enemy bullets

        for enemy in self.set_of_enemies:
            for attack in enemy.attacks:
                attack.update()
                enemy_bullets_group.add(attack)  # adding every bullet to enemy bullets group

        self.draw(self.surface)
        enemy_bullets_group.draw(self.surface)  # drawing enemy bullets

        # check collision between player and enemy bullet
        collided_bullets = pygame.sprite.spritecollide(self.player, enemy_bullets_group, True)
        for _ in collided_bullets:
            self.player.take_damage(3)  # deal 3 damage to player

        self.bad_touch()  # taking damage by colliding with enemy
        if self.player.health == 0:
            self.restart()

    def draw(self, screen) -> None:
        if self.doors and not self.set_of_enemies.spritedict:
            self.doors.draw(screen)
        self.buffs.draw(screen)
        self.obstacle_gen.draw(self.surface)
        self.set_of_enemies.draw(screen)

    # def pause(self):
    #     pass

    def bad_touch(self) -> None:  # taking damage by touching an enemy
        current_time = pygame.time.get_ticks()
        collided_enemy = pygame.sprite.spritecollideany(self.player, self.set_of_enemies)
        if pygame.sprite.spritecollideany(self.player, self.set_of_enemies):
            if current_time - self.last_damage_time >= 1000:  # interval between last taking damage
                self.player.take_damage(2)  # -2hp
                self.last_damage_time = current_time  # reset damage timer
            # self.set_of_enemies.remove(collided_enemy)  # remove collided enemy
            # collided_enemy.kill()

    def restart(self) -> None:
        self.player.health = 100
        self.buffs.empty()
        self.set_of_enemies.empty()
        self.obstacle_gen.obstacles.empty()
        self.obstacle_gen.traps.empty()
        self.new_level()


class Obstacles:

    def __init__(self, borders: tuple, difficulty: str = 'normal'):
        self.difficulty = difficulty
        self.borders = borders
        self.obstacles = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
        self.o_type = 'obs'

    def scale(self):
        if self.difficulty != 'normal':
            self.o_type = choices(['obs', 'trap'], weights=[2, 1], k=1)[0]
        else:
            self.o_type = 'obs'

    def version_1(self, image, difficulty: str = 'normal'):
        x0, x1, y0, y1 = 150, self.borders[0] - 150, 200, self.borders[1] - 200
        for _ in range(4):
            self.scale()
            self.craft_obstacle_or_trap(x0, y0, image, self.o_type)
            self.craft_obstacle_or_trap(x1, y1, image, self.o_type)
            x0 += 100
            x1 -= 100
        self.craft_obstacle_or_trap(self.borders[0] // 2, self.borders[1] // 2, image)

    def version2(self, image, difficulty: str = 'normal'):
        x, y = self.borders[0] // 2, self.borders[1] // 2 - 100
        x1, y1 = self.borders[0] // 2 - 100, self.borders[1] // 2
        for _ in range(3):
            self.scale()
            self.craft_obstacle_or_trap(x, y, image, self.o_type)
            self.craft_obstacle_or_trap(x1, y1, image, self.o_type)
            x1 += 100
            y += 100

    def version3(self, image, difficulty: str = 'normal'):
        x0, x1, y0, y1 = 150, self.borders[0] - 150, 200, self.borders[1] - 200
        for _ in range(4):
            self.scale()
            self.craft_obstacle_or_trap(x0, y0, image, self.o_type)
            self.craft_obstacle_or_trap(x1, y1, image, self.o_type)
            x0 += 300
            x1 -= 300

    def craft_obstacle_or_trap(self, cx: int, cy: int, image, o_type: str = 'obs') -> Character:
        new = Character(cx, cy, image, self.borders)
        if o_type == 'obs':
            self.obstacles.add(new)
        elif o_type == 'trap':
            self.traps.add(new)
        return new

    def draw(self, screen) -> None:
        self.obstacles.draw(screen)
        self.traps.draw(screen)

    def random_gen(self, image, difficulty: str = 'normal'):
        options = {0: print, 1: self.version_1, 2: self.version2, 3: self.version3}
        return options[randint(0, len(options) - 1)](image, difficulty)
