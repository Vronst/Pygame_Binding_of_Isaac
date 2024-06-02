from character import Character


class Enemy(Character):
    def __init__(self, cx, cy, image, borders, player, move_x, move_y):
        super().__init__(cx, cy, image, borders)
        self.player = player.rect
        self.move_x = move_x
        self.move_y = move_y
        self._moves = ((self.move_x, 0), (-self.move_x, 0), (0, self.move_y), (0, -self.move_y))
        self.melee = True

    def set_moves(self, x, y):
        self._moves = ((x, 0), (-x, 0), (0, y), (0, -y))

    def _move(self, group=None):
        # making it move dependent of player object
        distance_x = self.rect.x - self.player.x
        distance_y = self.rect.y - self.player.y
        if group:
            group = [x for x in group if x != self]

        moves = []

        if distance_x < 0 or (distance_x >= 0 and self.rect.x > self.borders[0] - 100 and not self.melee):
            # self.rect.move_ip(self._moves[0])
            moves.append(self._moves[0])
        if (distance_x > 0 or
                (distance_x >= 0 and self.rect.x < self.borders[0] - self.borders[0] + 100 and not self.melee)):
            # self.rect.move_ip(self._moves[1])
            moves.append(self._moves[1])
        if distance_y < 0:
            # self.rect.move_ip(self._moves[2])
            moves.append(self._moves[2])
        if distance_y > 0:
            # self.rect.move_ip(self._moves[3])
            moves.append(self._moves[3])

        for move in moves:
            self.rect.move_ip(move)
            for member in group:
                if self.rect.colliderect(member):
                    self.rect.move_ip(-move[0], -move[1])


class MeleeEnemy(Enemy):

    def __init__(self, cx, cy, image, borders, player, move_x=4, move_y=4):
        super().__init__(cx, cy, image, borders, player, move_x, move_y)

    def tired(self):
        pass


class RangeEnemy(Enemy):
    def __init__(self, cx, cy, image, borders, player, move_x=-3, move_y=5):
        super().__init__(cx, cy, image, borders, player, move_x, move_y)
        self.melee = False

    def attack(self):
        pass


