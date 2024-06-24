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
- collisions with obstacles

<br>Mateusz:

- audio and graphic research
- level design (obstacles and surfaces)
- menu
- class Item
- player (attack, health)
- collisions
- player animations

<br>To be allocated:

- enemies animations
- score
- boss (maybe in future)
- items (maybe in future)

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
- <a href=#button>Button</a>
- <a href=#ins>show_instructions</a>
- <a href=#about>show_about</a>
- <a href=#menu>main_menu</a>
- <a href=#obstacles>Obstacles</a>
- <a href=#item>Item</a>
- <a href=#heart>Heart</a>
- <a href=#bullet>EnemyBullet</a>
- <a href=#sword>PlayerSword</a>

---

<br><br>
<span id=overlay>`class Overlay(player, borders:tuple, images: dict, surfcace: pygame.Surface, background, direction=None, image=None, room=None)`</span> - class that creates and track <a href=#room>`rooms`</a> and room's <a href=#door>`doors`</a>. Initializing this class make one single room with doors that will create other ones. This class tracks them and allow to go back to rooms that were created. So going up, left, down and right will put you in a room in which you have started.

**Arguments**:

- _player_ -> <a href=#player>player</a> object
- _borders_ -> tuple with width and height of a window.
- _images_ -> dict that contains images with keys: 'MELEE_ENEMY' and 'RANGE_ENEMY'.
- _surface_ -> <a href="https://www.pygame.org/docs/ref/surface.html?highlight=surface#pygame.Surface">pygame.Surface</a> to draw enemies and obstacles on.
- _background_ -> path to image that will be used as background.
- _direction_ -> used to create door to previous <a href=#room>room</a>. It should contain information where the door should be placed.
- _image_ -> path to image that will be used as doors
- _room_ -> room that links with created doors (see direction argument)
  <br><br>

---

<span id=room>`class Room(player, borders: tuple, images: dict, surface: pygame.Surface,
                 background, direction=None, door_image=None, room=None, overlay=None, first=None)`</span> - this class creates <a href=#door>`doors`</a> and <a href=#detectcollision>`level`</a>. It also has its own coordinates which it creates from player cords. These cords are used to load it in proper location, and allowing player to get back to old rooms. <b>THIS OBJECT SHOULD NOT BE CREATED ON ITS OWN. USE <a href=#overlay>OVERLAY</a> INSTEAD.
</b>

**Arguments**:

- _player_ -> <a href=#player>player</a> object
- _borders_ -> tuple with width and height of a window.
- _images_ -> dict that contains images with keys: 'MELEE_ENEMY' and 'RANGE_ENEMY'.
- _surface_ -> <a href="https://www.pygame.org/docs/ref/surface.html?highlight=surface#pygame.Surface">pygame.Surface</a> to draw enemies and obstacles on.
- _background_ -> path to image that will be used as background.
- _direction_ -> used to create door to previous <a href=#room>room</a>. It should contain information where the door should be placed.
- _door_image_ -> path to image that will be used as doors.
- _room_ -> room that links with created doors (see direction argument).
- _overlay_ -> reference to overlay that contains all rooms. It allows navigation and after interacting with <a href=#door>door</a> allocation of proper room.
- _first_ -> if it is the first room, this argument is provided to the <a href=#detectcollision>level</a>

<br><br>
**Methods**:

- _check_the_door()_ -> returns <a href=#door>door</a> that player interacts with. Else returns False
- _is_in_door(door)_ -> uses doors go_thru().
- _init_door()_ -> creates random doors and specific doors (only if the room and the direction arguments are filled).
- _draw_ -> draws all doors that this room has.

---

<span id=door>`class Door(parent, image, position: str, borders: tuple, player, room=None, overlay=None)`</span> - this class is created by <a href=#room>Room</a> class. INSTEAD OF USING IT USE <a href=#overlay>OVERLAY</a> CLASS.

**Arguments**:

- _parent_ -> reference to Room object that created it.
- _image_ -> image of door.
- _position_ -> position in form of string. Based on it, it will have different coordinates.
- _borders_ -> tuple with width and height of a window.
- _player_ -> <a href=#player>player</a> object
- _room_ -> reference to <a href=#room>room</a>. It will teleport player to that room.
- _overlay_ -> reference of the main overlay

<br><br>
**Methods**:

- _go_thru()_ -> sets <a href=#player>Player</a> coords to the one that designated room has. It checks if the room exists and then use it. Otherwise, it creates new room. It also kills all player attacks.
- _draw(surface)_ -> draw itself on surface.

---

<span id=enemy>`class Enemy( cx, cy, image, borders, player, move_x, move_y, obstacles=None)`</span> - base for enemies. Inherits after <a href=#character>Character</a>
<br><br>
**Arguments**:

- _cx, cy, image, borders_ -> Same as parent class.
- _player_ -> <a href=#player>Player</a> object. It takes its coordinates, and use them to follow him.
- _move_x_ -> speed of movement on OX.
- _move_y_ -> speed of movement on OY.
- _obstacles_ -> list of obstacles that limits enemy movement

<br><br>
**Methods**:

- _attack_ -> not implemented.
- _is_melee_ -> returns self.\_melee.
- _tired()_ -> simple methods that returns True or False, used to stop this enemy from moving

---

<span id=meleeenemy>`class MeleeEnemy(cx, cy, image, borders, player, move_x=4, move_y=4, obstacles=None)`</span> - inherits after <a href=#enemy>Enemy</a>
<br><br>
**Arguments**:

- Same as parent class
- _player_ -> <a href=#player>Player</a> object. It takes its coordinates, and use them to follow him.
- _move_x_ -> look parent class.
- _move_y_ -> look parent class.
- _obstacles_ -> group of sprite that this object cannot move through.

<br><br>
**Methods**:

- _tired()_ -> simple methods that returns True or False, used to stop this enemy from moving

---

<span id=rangeenemy>`class RangeEnemy(cx, cy, image, borders, player, move_x=3, move_y=5, obstacles=None)`</span> - inherits after <a href=#enemy>Enemy</a>
<br><br>
**Arguments**:

- Same as parent class
- _player_ -> <a href=#player>Player</a> object. It takes its coordinates, and use them to follow and shoot him
- _move_x_ -> look parent class
- _move_y_ -> look parent class

<br><br>
**Methods**:

- _attack()_ -> creates <a href=#bullet>Bullet</a> object.

---

<span id=character>`class Character(cx, cy, image, borders, obstacles=None)`</span> - it is the base for any character either player or enemy. Inherits after [pygame.sprite.Sprite](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite)
<br><br>
**Arguments**:

- _cx_ -> x-coordinate
- _cy_ -> y-coordinate
- _image_ -> image which this object will represent
- _borders_ -> coordinates which this object cannot cross _(default (1200, 800))_
- _obstacles_ -> list of obstacles --no use for this because it is not implemented in this class
  <br><br>

**Methods**:

- _get_event(\*\*kwargs)_ -> to implement in inheriting classes
- _draw_ -> puts object on screen
- _update(key_pressed)_ -> passes key_pressed to get_event(), ensures that object won't cross borders
- _tired()_ -> returns false. (Important in enemy design)

---

<span id=player>`class Player(cx, cy, images, border: tuple, obstacles=None, traps=None, weapon=None)`</span> - inherits after <a href=#character>Character</a>
<br><br>
**Arguments**:

- _cx_ -> x-coordinate.
- _cy_ -> y-coordinate.
- _image_ -> image which this object will represent.
- _borders_ -> borders of the window _(default (1200, 800))_.
- _obstacles_ -> list of obstacles.
- _traps_ -> list of traps (obstacles that damage player).
- _weapon_ -> image for weapon.
  <br><br>

**Methods**:

- _get_event(\*\*kwargs)_ -> reads keys that player presses and moves character. Also animates it.
- _draw(display)_ -> puts object and health bar on screen
- _draw_health_bar(display)_ -> used by _draw(display)_ to draw health bar.
- _take_damage(amount)_ -> reduces health by amount
- _heal(amount)_ -> increases health by amount
- _check_collision(self, move)_ -> checks if player collided with obstacle or trap and either block the move or damages player
- _attack_ -> creates object of <a href=#sword>PlayerWeapon</a> and adds it to self.attacks (pygame group).

---

<span id=detectcollision>`class Level(player: Character, borders: tuple, images: dict, surface: pygame.Surface, background, doors=None, first=None)`</span> - this class is used to create and control one single <a href=#room>`room`</a>. It spawns and updates <a href=#enemy>`enemies`</a>. It also controls player movement, so he wont leave screen. <br>
<br><br>
**Arguments**:

- _player_ -> <a href=#player>Player</a> object.
- _borders_ -> borders of the window
- _images_ -> dict containing images loaded by pygame and converted with <a href="https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha">convert_alpha()</a>
- _surface_ -> pygame surface that. Used as a screen to draw objects.
- _background_ -> background image.
- _doors_ -> doors object to be drawn.
- _first_ -> if True, there will be no obstacles and no enemies in the room
  <br><br>

**Methods**:

- _new_level()_ -> spawns random number of enemies, then preset of obstacles, and existing doors and draws them.
- _draw(display)_ -> puts objects and health bar on screen.
- _update()_ -> updates buffs, enemies and bullets then draws them. Checks for collision with bullets and enemies. Also monitors health.
- _bad_touch()_ -> checks for collision with enemies and if it occurs kills them and damages player (with cooldown)
- _restart()_ -> resets player health, deletes buffs, enemies and obstacles and then generates new level.

---

<span id=button>`class Button(text, pos, font, text_color=BLACK, hover_text_color=WHITE, bg_color=GRAY, hover_bg_color=DARK_GRAY, border_color=BLACK)`</span> - creates functional button.
<br><br>
**Arguments**:

- _text_ -> text that will be displayed on button.
- _pos_ -> position for the button to appear.
- _font_ -> font that button's text will use.
- _text_color_ -> color of the text.
- _hover_text_color_ -> text color when hovered. Default black.
- _bg_color_ -> button background color.
- _hover_bg_color_ -> button background color when hovered. Default gray.
- _border_color_ -> color of button's borders. Default black.
  <br><br>

**Methods**:

- _change_text()_ -> creates rect for button and fills it with designated color. Puts text on button.
- _show()_ -> changes button when hovered.
- _click()_ -> checks if button were clicked.

---

<span id=obstacles>`class Obstacles(borders: tuple, difficulty: str = 'normal)`</span> - This class generates obstacles and traps (not implemented yet).

<br><br>
**Arguments**:

- _borders_ -> area for obstacles to be generated
- _difficulty_ -> not implemented, better to stay 'normal'

**Methods**:

- _scale()_ -> based on difficulty chooses if generated object is trap or obstacle
- _version{**number**}()_ -> Predefined layout.
- _craft_obstacle_or_trap()_ -> Creates object. It could be a trap if difficulty was different then normal and scale() was used.
- _draw(screen)_ -> draws obstacles and traps on screen.
- _random_gen(image, difficulty: str = 'normal')_ -> run this to generate random layout form predefined layouts (version{number}).

---

<span id=item>`class Item(cx, cy, image, borders)`</span> - this class is blueprint for vast items.

<br><br>
**Arguments**:

- _cx_ -> x coordinate.
- _cy_ -> y coordinate.
- _imgage_ -> image of item.
- _borders_ -> game window size.

**Methods**:

- _update(key_pressed=None, group=None, obstacles=None, borders: tuple = (1200, 800)_ -> uses self.\_move()

---

<span id=heart>`class Heart(image, borders)`</span> - item that heals player.

<br><br>
**Arguments**:

- _imgage_ -> image of item.
- _borders_ -> game window size in which it can spawn.

**Methods**:

- _spawn()_ -> spawns in random position.
- _heal(player)_ -> uses player.heal(5).

---

<span id=ins>`def show_instructions()`</span> - show instruction screen.

---

<span id=about>`def show_about()`</span> - show about screen.

---

<span id=menu>`def main_menu()`</span> - renders buttons (start, about, instructions and quit). Draws menu screen.

---

<span id=bullet>`class EnemyBullet(cx, cy, image, borders: tuple, direction: str, speed=3)`</span> - bullet for enemies to use.

<br><br>
**Arguments**:

- _cx_ -> x coordinate.
- _cy_ -> y coordinate.
- _imgage_ -> image of item.
- _borders_ -> game window size.
- _direction_ -> direction that bullet follows.
- _speed_ -> speed of traveling.

---

<span id=sword>`class PlayerSword(cx, cy, image, borders, direction: str, speed=3, range=100, owner=None)`</span> - Only object that allows player to attack.

<br><br>
**Arguments**:

- _cx_ -> x coordinate.
- _cy_ -> y coordinate.
- _imgage_ -> image of item.
- _borders_ -> game window size.
- _direction_ -> direction of attack.
- _speed_ -> speed of attack.
- _range_ -> range of attack.

**Methods**:

- _update(surface)_ -> uses self.\_move() and self.draw().

---

<span id=immune>def immune(self) -> bool:</span> - function checks if object been hit, if so returns true.

---
