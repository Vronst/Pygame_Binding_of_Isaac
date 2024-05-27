import os
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 800))
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


# main loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # place for game code

pygame.quit()
