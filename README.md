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


<br>Mateusz:
- audio
- menu

<br>To be allocated:
- enemies (ranged attack)
- player (attack, health)
- level design (obstacles and surfaces)
- collisions with other objects
- trap doors?
---

### Documentation
<br>
<a href="https://www.pygame.org/docs/">Pyggame documentation</a>

<br><br>
Table of content:
- <a href=#character>Character</a>
- <a href=#meleeenemy>MeleeEnemy</a>
- <a href=#rangeenemy>RangeEnemy</a>
- <a href=#detectcollision>DetectCollision</a>

---
<br><br>
<span id=character>`class Character(cx, cy, image, borders)`</span> - it is the base for any character either player or enemy. Inherits after [pygame.sprite.Sprite](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite)
<br><br>
**Arguments**:
- *cx* -> x-coordinate
- *cy* -> y-coordinate
- *image* -> image which this object will represent
- *borders* -> coordinates which this object cannot cross *(default (1200, 800))*
<br><br>

**Methods**:
- *get_event(\*\*kwargs)* -> to implement in inheriting classes 
- *draw* -> puts object on screen
- *update(key_pressed)* -> passes key_pressed to get_event(), ensures that object won't cross borders
---
<span id=meleeenemy>`class MeleeEnemy(cx, cy, image, borders, player)`</span> - inherits after <a href=#character>Character</a>
<br><br>
**Arguments**:
- Same as parent class
- player -> other Character object. It takes its coordinates, and use them to follow him
---

<span id=detectcollision>`class DetectCollision(player: Character, borders: tuple)`</span>

---
<span id=rangeenemy>`class RangeEnemy(cx, cy, image, borders, player)`</span>