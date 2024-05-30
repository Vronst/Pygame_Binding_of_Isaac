from character import Character


class MeleeEnemy(Character):

    def __init__(self, cx, cy, image, borders, player):
        super().__init__(cx, cy, image, borders)
        self.player = player.rect

    def _move(self):
        distance_x = self.rect.x - self.player.x
        distance_y = self.rect.y - self.player.y
        # print(self.player, self.rect.top, self.rect.left, self.rect.bottom)
        if distance_x < 0:
            self.rect.move_ip([5, 0])
        elif distance_x > 0:
            self.rect.move_ip([-5, 0])
        if distance_y < 0:
            self.rect.move_ip([0, 5])
        elif distance_y > 0:
            self.rect.move_ip([0, -5])

