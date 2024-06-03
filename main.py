import os
import pygame
from player import Player
from level import DetectCollision

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
BACKGROUND = pygame.image.load(os.path.join(path, 'level-background.jpg')).convert()
file_names.remove('background.jpg')
IMAGES = {}

game_music_path = os.path.join('music', 'nojisuma - hallucination.mp3') #game music path
pygame.mixer.music.stop() #stop previous music
pygame.mixer.music.load(game_music_path) #load game music
pygame.mixer.music.play(-1) #play the game music in a loop
pygame.mixer.music.set_volume(0.5) #setting volume

# get dict with img names and converted img
for file_name in file_names:
    image_name = file_name[:-4].upper()
    # convert_alpha() is for fast blit into desired surface that's why no normal convert()
    IMAGES[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(BACKGROUND)

player = Player(DISPLAY[0] / 2, DISPLAY[1] / 2, IMAGES['PLAYER'], DISPLAY)
# enemy = MeleeEnemy(100, 100, IMAGES['PLAYER'], DISPLAY, player)
# enemy1 = RangeEnemy(100, 300, IMAGES['PLAYER'], DISPLAY, player, -3, 5)
level = DetectCollision(player, DISPLAY, IMAGES, screen, BACKGROUND)
level.new_level()

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

    level.update()  # moving enemies
    level.draw(screen)
    player.update(pygame.key.get_pressed())
    player.draw(screen)
    pygame.display.update()

    # lets make it 60fps
    clock.tick(60)
pygame.quit()
