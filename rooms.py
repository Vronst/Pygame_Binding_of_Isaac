import pygame
import random
from level import DetectCollision

"""
First create Room that uses DetectCollision and creates its own doors.
Then these doors create new Rooms. New rooms have designated doors that stores previous doors
"""


class Room:

    def __init__(self, player, borders: tuple, images: dict, surface: pygame.Surface,
                 background, direction=None, image=None, room=None):
        self.room = room
        self.background = background
        self.surface = surface
        self.images = images
        self.borders = borders
        self.player = player
        self.door_image = image
        self.rect = self.door_image.get_rect()
        self.doors = pygame.sprite.Group()  # should be group
        self.direction = {'top': 'bottom', 'bottom': 'top', 'left': 'right', 'right': 'left', None: None}[direction]
        self.level = DetectCollision(self.player, self.borders, self.images, self.surface, self.background, doors=self.doors)
        self.init_door()

    def init_door(self):
        direction = ['top', 'right', 'bottom', 'left']
        if self.direction:
            direction.remove(self.direction)
        current_set = set()
        for _ in range(6):
            current_set.add(random.choice(direction))
        for x in current_set:
            door = Door(self, self.door_image, x, self.level.borders)
            self.doors.add(door)
        if self.room is not None:
            self.doors.add(Door(self, self.door_image, self.direction, self.borders, room=self.room))

    def join(self, direction: str):
        pass

    def draw(self):
        self.surface.blit(self.door_image, self.rect)


class Door(pygame.sprite.Sprite):

    def __init__(self, parent, image, position: str, borders: tuple, room=None):
        super().__init__()
        self.room = room
        self.parent = parent
        self.where = position
        self.image = image
        self.rect = self.image.get_rect()
        # dict for quick position reading
        self.position = {'top': (borders[0] // 2, 10), 'bottom': (borders[0] // 2, borders[1]-10),
                         'left': (50, borders[1] // 2), 'right': (borders[0] - 50, borders[1] // 2)}
        self.rect = self.image.get_rect()
        # setting position
        self.rect.center = self.position[position]

    def go_thru(self):
        if self.room:
            return self.room
        return Room(self.parent.parent, self.parent.player, self.parent.borders,
                    self.parent.images, self.parent.surface, self.parent.background,
                    direction=self.where, room=self.parent)

    def door_direction(self):
        return self.where

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# class Map:
#
#     def __init__(self, difficulty: int, player, borders: tuple, images: dict, surface: pygame.Surface,
#                  background) -> None:
#         self.background = background
#         self.surface = surface
#         self.images = images
#         self.borders = borders
#         self.player = player
#         self.difficulty = difficulty
#         self.rooms = []
#         self.current_level = None
#
#     def new_map(self, direction=None):
#         self.rooms.append(Room(self,
#                                DetectCollision(self.player,
#                                                self.borders,
#                                                self.images,
#                                                self.surface,
#                                                self.background,
#                                                ),
#                                direction=direction))
#         self.current_level = self.rooms[-1]
#
#     def add_room(self, room):
#         self.rooms.append(room)
