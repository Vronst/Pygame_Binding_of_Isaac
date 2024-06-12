## Pygame [The Binding of Isaac](https://store.steampowered.com/app/113200/The_Binding_of_Isaac/)

### This project was created to fulfill the requirements for a coursein object-oriented programming at university. It was developed by me, Adam Sarga (Vronst), and Mateusz Ryszawy.
<br><br>
This is an overview of our project. For more details, see the following sections:
- [Description](#Description)
- <a href=#allocation>Allocation of work</a>
- [Documentation](#Documentation)


### Description

<br>The idea of this project is to create something similar to popular game with the name in title of this project.
<br><br><br>
---
#### <span id=allocation>Project work allocation</span>:
<br>Adam:
- class Character
- player (movement)
- enemies (melee)
- enemy collision
- doors and rooms
- enemies (ranged attack, no graphic)
- readme
- obstacles layout and generation

<br>Mateusz:
- audio and graphic research
- menu
- class Item
- player (attack, health)
- collisions
- simple player idle animation (for now)

<br>To be allocated:

- enemies animations
- level design (obstacles and surfaces)
- collisions with obstacles
---

### Documentation
<br>
<a href="https://www.pygame.org/docs/">Pygame documentation</a>

<br><br>
Table of content:
- <a href=#overlay>Overlay</a>
- <a href=#room>Room</a>
- <a href=#door>Door</a>
- <a href=#enemy>Enemy</a>
- <a href=#meleeenemy>MeleeEnemy</a>
- <a href=#rangeenemy>RangeEnemy</a>
- <a href=#character>Character</a>
- <a href=#player>Player</a>
- <a href=#detectcollision>Level</a>
- <a href=#bullet>Bullet</a>
- <a href=#button>Button</a>
- <a href=#ins>show_instructions()</a>
- <a href=#about>show_about()</a>
- <a href=#menu>main_menu()</a>
- <a href=#obstacles>Obstacles()</a>

---
<br><br>
<span id=overlay>`class Overlay(player, borders:tuple, images: dict, surfcace: pygame.Surface, background, direction=None, image=None, room=None)`</span> - class that creates and track <a href=#room>`rooms`</a> and room's <a href=#door>`doors`</a>. Initializing this class make one single room with doors that will create other ones. This class tracks them and allow to go back to rooms that were created. So going up, left, down and right will put you in a room in which you have started.

**Arguments**:
- *player* -> <a href=#player>player</a> object
- *borders* -> tuple with width and height of a window.
- *images* -> dict that contains images with keys: 'MELEE_ENEMY' and 'RANGE_ENEMY'.
- *surface* -> <a href="https://www.pygame.org/docs/ref/surface.html?highlight=surface#pygame.Surface">pygame.Surface</a> to draw enemies and obstacles on.
- *background* -> path to image that will be used as background.
- *direction* -> used to create door to previous <a href=#room>room</a>. It should contain information where the door should be placed.
- *image* -> path to image that will be used as doors
- *room* -> room that links with created doors (see direction argument)
<br><br>
---
<span id=room>`class Room(player, borders: tuple, images: dict, surface: pygame.Surface,
                 background, direction=None, door_image=None, room=None, overlay=None, first=None)`</span> - this class creates <a href=#door>`doors`</a> and <a href=#detectcollision>`level`</a>. It also has its own coordinates which it creates from player cords. These cords are used to load it in proper location, and allowing player to get back to old rooms. <b>THIS OBJECT SHOULD NOT BE CREATED ON ITS OWN. USE <a href=#overlay>OVERLAY</a> INSTEAD.
</b>

**Arguments**:
- *player* -> <a href=#player>player</a> object
- *borders* -> tuple with width and height of a window.
- *images* -> dict that contains images with keys: 'MELEE_ENEMY' and 'RANGE_ENEMY'.
- *surface* -> <a href="https://www.pygame.org/docs/ref/surface.html?highlight=surface#pygame.Surface">pygame.Surface</a> to draw enemies and obstacles on.
- *background* -> path to image that will be used as background.
- *direction* -> used to create door to previous <a href=#room>room</a>. It should contain information where the door should be placed.
- *door_image* -> path to image that will be used as doors.
- *room* -> room that links with created doors (see direction argument).
- *overlay* -> reference to overlay that contains all rooms. It allows navigation and after interacting with <a href=#door>door</a> allocation of proper room.
- *first* -> if it is the first room, this argument is provided to the <a href=#detectcollision>level</a>

<br><br>
**Methods**:
- *check_the_door()* -> returns <a href=#door>door</a> that player interacts with. Else returns False
- *is_in_door(door)* -> uses doors go_thru().
- *init_door()* -> creates random doors and specific doors (only if the room and the direction arguments are filled).
- *draw* -> draws all doors that this room has.
---
<span id=door>`class Door(parent, image, position: str, borders: tuple, player, room=None, overlay=None)`</span> - this class is created by <a href=#room>Room</a> class. INSTEAD OF USING IT USE <a href=#overlay>OVERLAY</a> CLASS.

**Arguments**:
- *parent* -> reference to Room object that created it.
- *image* -> image of door.
- *position* -> position in form of string. Based on it, it will have different coordinates.
- *borders* -> tuple with width and height of a window.
- *player* -> <a href=#player>player</a> object
- *room* -> reference to <a href=#room>room</a>. It will teleport player to that room.
- *overlay* -> reference of the main overlay

<br><br>
**Methods**:
- *go_thru()* -> sets <a href=#player>Player</a> coords to the one that designated room has. It checks if the room exists and then use it. Otherwise, it creates new room.
- *draw(surface)* -> draw itself on surface.
---
<span id=enemy>`class Enemy( cx, cy, image, borders, player, move_x, move_y, obstacles=None)`</span> - base for enemies. Inherits after <a href=#character>Character</a>
<br><br>
**Arguments**:
- *cx, cy, image, borders* -> Same as parent class.
- *player* -> <a href=#player>Player</a> object. It takes its coordinates, and use them to follow him.
- *move_x* -> speed of movement on OX.
- *move_y* -> speed of movement on OY.
- *obstacles* -> list of obstacles that limits enemy movement

<br><br>
**Methods**:
- *tired()* -> simple methods that returns True or False, used to stop this enemy from moving
---
<span id=meleeenemy>`class MeleeEnemy(cx, cy, image, borders, player, move_x=4, move_y=4)`</span> - inherits after <a href=#enemy>Enemy</a>
<br><br>
**Arguments**:
- Same as parent class
- *player* -> <a href=#player>Player</a> object. It takes its coordinates, and use them to follow him
- *move_x* -> look parent class
- *move_y* -> look parent class

<br><br>
**Methods**:
- *tired()* -> simple methods that returns True or False, used to stop this enemy from moving
---
<span id=rangeenemy>`class RangeEnemy(cx, cy, image, borders, player)`</span> - inherits after <a href=#enemy>Enemy</a>
<br><br>
**Arguments**:
- Same as parent class
- *player* -> <a href=#player>Player</a> object. It takes its coordinates, and use them to follow and shoot him
- *move_x* -> look parent class
- *move_y* -> look parent class

<br><br>
**Methods**:
- *attack()* -> creates <a href=#bullet>Bullet</a> object.
---

<span id=character>`class Character(cx, cy, image, borders, obstacles=None)`</span> - it is the base for any character either player or enemy. Inherits after [pygame.sprite.Sprite](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite)
<br><br>
**Arguments**:
- *cx* -> x-coordinate
- *cy* -> y-coordinate
- *image* -> image which this object will represent
- *borders* -> coordinates which this object cannot cross *(default (1200, 800))*
- *obstacles* -> list of obstacles --no use for this because it is not implemented in this class
<br><br>

**Methods**:
- *get_event(\*\*kwargs)* -> to implement in inheriting classes 
- *draw* -> puts object on screen
- *update(key_pressed)* -> passes key_pressed to get_event(), ensures that object won't cross borders
---
<span id=player>`class Player(cx, cy, images, border: tuple, obstacles=None, traps=None)`</span> - inherits after <a href=#character>Character</a>
<br><br>
**Arguments**:
- *cx* -> x-coordinate.
- *cy* -> y-coordinate.
- *image* -> image which this object will represent.
- *borders* -> borders of the window *(default (1200, 800))*.
- *obstacles* -> list of obstacles.
- *traps* -> list of traps (obstacles that damage player).
<br><br>

**Methods**:
- *get_event(\*\*kwargs)* -> reads keys that player presses and moves character. Also animates it.
- *draw(display)* -> puts object and health bar on screen
- *draw_health_bar(display)* -> used by *draw(display)* to draw health bar.
- *take_damage(amount)* -> reduces health by amount
- *heal(amount)* -> increases health by amount
- *check_collision(self, move)* -> checks if player collided with obstacle or trap and either block the move or damages player
---
<span id=detectcollision>`class Level(player: Character, borders: tuple, images: dict, surface: pygame.Surface, background, doors=None, first=None)`</span> - this class is used to create and control one single <a href=#room>`room`</a>. It spawns and updates <a href=#enemy>`enemies`</a>. It also controls player movement, so he wont leave screen. <br>
<br><br>
**Arguments**:
- *player* ->  <a href=#player>Player</a> object.
- *borders* -> borders of the window
- *images* -> dict containing images loaded by pygame and converted with <a href="https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha">convert_alpha()</a>
- *surface* -> pygame surface that. Used as a screen to draw objects.
- *background* -> background image.
- *doors* -> doors object to be drawn.
- *first* -> if True, there will be no obstacles and no enemies in the room
<br><br>

**Methods**:
- *new_level()* -> spawns random number of enemies, then preset of obstacles, and existing doors and draws them.
- *draw(display)* -> puts objects and health bar on screen.
- *update()* -> updates buffs, enemies and bullets then draws them. Checks for collision with bullets and enemies. Also monitors health.
- *bad_touch()* -> checks for collision with enemies and if it occurs kills them and damages player (with cooldown)
- *restart()* -> resets player health, deletes buffs, enemies and obstacles and then generates new level.
---
<span id=button>`class Button(text, pos, font, text_color=BLACK, hover_text_color=WHITE, bg_color=GRAY, hover_bg_color=DARK_GRAY, border_color=BLACK)`</span> - creates functional button.
<br><br>
**Arguments**:
- *text* -> text that will be displayed on button.
- *pos* -> position for the button to appear.
- *font* -> font that button's text will use.
- *text_color* -> color of the text.
- *hover_text_color* -> text color when hovered. Default black.
- *bg_color* -> button background color.
- *hover_bg_color* -> button background color when hovered. Default gray.
- *border_color* -> color of button's borders. Default black.
<br><br>

**Methods**:
- *change_text()* -> creates rect for button and fills it with designated color. Puts text on button.
- *show()* -> changes button when hovered.
- *click()* -> checks if button were clicked.
---

<span id=obstacles>`class Obstacles(borders: tuple, difficulty: str = 'normal)`</span> - This class generates obstacles and traps (not implemented yet).

<br><br>
**Arguments**:
- *borders* -> area for obstacles to be generated
- *difficulty* -> not implemented, better to stay 'normal'


**Methods**:
- *scale()* -> based on difficulty chooses if generated object is trap or obstacle
- *version{**number**}()* -> Predefined layout.
- *craft_obstacle_or_trap()* -> Creates object. It could be a trap if difficulty was different then normal and scale() was used.
- *draw(screen)* -> draws obstacles and traps on screen.
- *random_gen(image, difficulty: str = 'normal')* -> run this to generate random layout form predefined layouts (version{number}).

---

<span id=ins>`def show_instructions()`</span> - show instruction screen.

---

<span id=about>`def show_about()`</span> - show about screen.

---

<span id=menu>`def main_menu()`</span> - renders buttons (start, about, instructions and quit). Draws menu screen.

---