import random


class Sheep:
    def __init__(self, id, limit, distance):
        self.id = id
        self.init_pos_limit = limit
        self.position = [random.uniform(-self.init_pos_limit, self.init_pos_limit),
                         random.uniform(-self.init_pos_limit, self.init_pos_limit)]
        self.sheep_move_dist = distance

    def print_sheep(self):
        print("Owca nr " + str(self.id+1) + " znajduje sie na pozycji " + str(self.position))

    def move_sheep(self):
        direction = random.randint(0,3)
        if direction == 0:
            self.position[1] += self.sheep_move_dist
        elif direction == 1:
            self.position[0] += self.sheep_move_dist
        elif self.position == 2:
            self.position[1] += -self.sheep_move_dist
        else:
            self.position[0] += self.sheep_move_dist
