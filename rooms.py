import pygame
import random
from level import DetectCollision


class Room:

    def __init__(self, parent, level, direction=None, image=None):
        self.door_image = image
        self.doors = []  # should be list
        self.level = level
        self.direction = direction
        self.parent = parent
        self.init_door()

    def init_door(self):
        direction = ('top', 'right', 'bottom', 'left')
        current_set = set()
        for _ in range(4):
            current_set.add(random.choice(direction))
        for x in current_set:
            door = Door(self.door_image, x, self.level.borders)
            self.doors.append(door)

    def join(self, direction: str):
        self.parent.new_map()


class Door(pygame.sprite.Sprite):

    def __init__(self, image, position: str, borders: tuple, direction: dict = None):
        super().__init__()
        self.where = position
        self.rooms = {'top': None, 'bottom': None, 'left': None, 'right': None}
        self.image = image
        self.rect = self.image.get_rect()
        # dict for quick position reading
        self.position = {'top': (borders[0] // 2, 0), 'bottom': (borders[0] // 2, borders[1]),
                         'left': (0, borders[1] // 2), 'right': (0, borders[1] // 2)}
        self.rect = self.image.get_rect()
        # setting position
        self.rect.center = self.position[position]

    def door_direction(self):
        return self.where


class Map:

    def __init__(self, difficulty: int, player, borders: tuple, images: dict, surface: pygame.Surface,
                 background) -> None:
        self.background = background
        self.surface = surface
        self.images = images
        self.borders = borders
        self.player = player
        self.difficulty = difficulty
        self.rooms = []
        self.current_level = None

    def new_map(self, direction=None):
        self.rooms.append(Room(self,
                               DetectCollision(self.player,
                                               self.borders,
                                               self.images,
                                               self.surface,
                                               self.background,
                                               ),
                               direction=direction))
        self.current_level = self.rooms[-1]

    def add_room(self, room):
        self.rooms.append(room)
