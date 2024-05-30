import os
import pygame
from player import Player

# pygame setup
DISPLAY = (1200, 800)
pygame.init()
screen = pygame.display.set_mode(DISPLAY)
clock = pygame.time.Clock()
running = True

# code from teachers example
# getcwd() gives path to current directory, so we join it with folder with images that we want to load
path = os.path.join(os.getcwd(), 'images')

# os.listdir shows files in chosen directory
file_names = os.listdir(path)

# preparing background
BACKGROUND = pygame.image.load(os.path.join(path, 'background.jpg')).convert()
file_names.remove('background.jpg')
IMAGES = {}

# get dict with img names and converted img
for file_name in file_names:
    image_name = file_name[:-4].upper()
    # convert_alpha() is for fast blit into desired surface that's why no normal convert()
    IMAGES[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(BACKGROUND)

player = Player(100, 100, IMAGES['TEST'], DISPLAY)

# main loop
while running:

    screen.blit(pygame.transform.scale(BACKGROUND, DISPLAY), (0, 0))
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        if event.type == pygame.QUIT:
            running = False

    player.update(pygame.key.get_pressed())
    player.draw(screen)
    pygame.display.update()

pygame.quit()
