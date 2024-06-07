import pygame
import random
from level import DetectCollision

"""
First create Room that uses DetectCollision and creates its own doors.
Then these doors create new Rooms. New rooms have designated doors that stores previous doors
"""


class Room:

    def __init__(self, player, borders: tuple, images: dict, surface: pygame.Surface,
                 background, direction=None, door_image=None, room=None, overlay=None):
        self.overlay = overlay
        self.room = room
        self.background = background
        self.surface = surface
        self.images = images
        self.borders = borders
        self.player = player
        self.door_image = door_image if door_image else room.door_image
        self.rect = self.door_image.get_rect()
        self.doors = pygame.sprite.Group()  # should be a group
        self.direction = {'top': 'bottom', 'bottom': 'top', 'left': 'right', 'right': 'left', None: None}[direction]
        self.level = DetectCollision(self.player, self.borders, self.images,
                                     self.surface, self.background, doors=self.doors)
        self.init_door()
        self.room_cords = self.player.cords

    def check_the_door(self):
        for door in self.doors:
            if self.player.rect.colliderect(door):
                return door
        return False

    def is_in_door(self, door):
        return door.go_thru()

    def init_door(self):
        direction = ['top', 'right', 'bottom', 'left']
        if self.direction:
            direction.remove(self.direction)
        current_set = set()
        for _ in range(6):  # increase range for higher average of doors and decrease for lower
            current_set.add(random.choice(direction))
        for x in current_set:
            door = Door(self, self.door_image, x, self.level.borders, self.player, overlay=self.overlay)
            self.doors.add(door)
        if self.room is not None:
            door = Door(self, self.door_image, self.direction,
                        self.borders, self.player, room=self.room, overlay=self.overlay)
            self.doors.add(door)

    # def join(self, direction: str):
    #     pass

    def draw(self):
        self.surface.blit(self.door_image, self.rect)


class Door(pygame.sprite.Sprite):

    def __init__(self, parent, image, position: str, borders: tuple, player, room=None, overlay=None):
        super().__init__()
        self.overlay = overlay
        self.room = room
        self.parent = parent
        self.where = position
        self.image = image
        self.rect = self.image.get_rect()
        # dict for quick position reading
        self.position = {'top': (borders[0] // 2, 10), 'bottom': (borders[0] // 2, borders[1] - 10),
                         'left': (50, borders[1] // 2), 'right': (borders[0] - 50, borders[1] // 2)}
        self.rect = self.image.get_rect()
        # setting position
        self.rect.center = self.position[position]
        self.cords = {'top': (player.cords[0], player.cords[1] + 1),
                      'bottom': (player.cords[0], player.cords[1] - 1),
                      'left': (player.cords[0] - 1, player.cords[1]),
                      'right': (player.cords[0] + 1, player.cords[1])}[self.where]

    def go_thru(self):
        for room in self.overlay.rooms:
            if room.room_cords == self.cords:
                self.parent.player.cords = self.cords
                return room
        self.parent.player.cords = self.cords
        room = Room(player=self.parent.player, borders=self.parent.borders,
                    images=self.parent.images, surface=self.parent.surface, background=self.parent.background,
                    direction=self.where,
                    door_image=self.image, room=self.parent, overlay=self.overlay)
        # (self, player, borders: tuple, images: dict, surface: pygame.Surface,
        #                  background, direction=None, image=None, room=None, overlay=None):
        self.overlay.rooms.append(room)
        self.overlay.current_room = room
        return room

    def door_direction(self):
        return self.where

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Overlay:

    def __init__(self, player, borders: tuple, images: dict, surface: pygame.Surface,
                 background, direction=None, image=None, room=None):
        self.rooms = []
        self.rooms.append(Room(player, borders, images, surface,
                               background, direction, image, room, overlay=self))
        self.current_room = self.rooms[0]

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
