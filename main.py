import os
import pygame
from player import Player
from item import Heart
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

game_music_path = os.path.join('music', 'nojisuma - hallucination.mp3')  #game music path
pygame.mixer.music.stop()  #stop previous music
pygame.mixer.music.load(game_music_path)  #load game music
pygame.mixer.music.play(-1)  #play the game music in a loop
pygame.mixer.music.set_volume(0.5)  #setting volume

# get dict with img names and converted img
for file_name in file_names:
    image_name = file_name[:-4].upper()
    # convert_alpha() is for fast blit into desired surface that's why no normal convert()
    IMAGES[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(BACKGROUND)

player_images = []
for i in range(1, 6):  # 5 images: hero_idle_01.png to hero_idle_08.png
    image_name = f'hero_idle_{i:02}.png'
    player_images.append(pygame.image.load(os.path.join(path, image_name)).convert_alpha())

heart_image = pygame.image.load(os.path.join(path, 'heart.png'))  #heart image

player = Player(DISPLAY[0] / 2, DISPLAY[1] / 2, player_images, DISPLAY)
# enemy = MeleeEnemy(100, 100, IMAGES['PLAYER'], DISPLAY, player)
# enemy1 = RangeEnemy(100, 300, IMAGES['PLAYER'], DISPLAY, player, -3, 5)
level = DetectCollision(player, DISPLAY, IMAGES, screen, BACKGROUND)
level.new_level()

last_health_update = pygame.time.get_ticks()  # time from start of the game
last_item_spawn = pygame.time.get_ticks()  # time from start of the game
item_spawn_interval = 1000

hearts = pygame.sprite.Group()  # group of hearts on the screen

collision_detector = DetectCollision(player, DISPLAY, IMAGES, screen, None)
# collision detector between player and enemies


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

    current_time = pygame.time.get_ticks()  #time from start of the game
    if current_time - last_item_spawn >= item_spawn_interval:
        new_heart = Heart(heart_image, DISPLAY)  #create new heart objcet
        hearts.add(new_heart)  #add new_heart to hearts group
        last_item_spawn = current_time  #reset spawn timer

    collided_hearts = pygame.sprite.spritecollide(player, hearts,
                                                  True)  #check collides between heart and player and delete collided heart from hearts group, adding it to collided hearts
    for heart in collided_hearts:
        heart.heal(player)  #heal from collided heart

    level.update()  # moving enemies
    player.update(pygame.key.get_pressed())

    level.draw(screen)
    player.draw(screen)
    hearts.draw(screen)
    pygame.display.update()

    # lets make it 60fps
    clock.tick(60)
pygame.quit()
