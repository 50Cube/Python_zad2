import random
import logging


class Sheep:
    def __init__(self, id, limit, distance):
        logging.debug('sheep.__init__(id=' + str(id) +
                      ', limit=' + str(limit) +
                      ' distance=' + str(distance) + ')')
        self.id = id
        self.init_pos_limit = limit
        self.position = [random.uniform(-self.init_pos_limit, self.init_pos_limit),
                         random.uniform(-self.init_pos_limit, self.init_pos_limit)]
        logging.info('Ustalenie pozycji poczatkowej owcy nr ' + str(id) + ': (' + str(self.position[0]) + '; ' + str(self.position[1]) + ')')
        self.sheep_move_dist = distance

    def print_sheep(self):
        logging.debug('sheep.print_sheep()')
        print("Owca nr " + str(self.id+1) + " znajduje sie na pozycji " + str(self.position))

    def move_sheep(self):
        logging.debug('sheep.move_sheep()')
        old_pos = [self.position[0], self.position[1]]
        direction = random.randint(0, 3)
        if direction == 0:
            self.position[1] += self.sheep_move_dist
        elif direction == 1:
            self.position[0] += self.sheep_move_dist
        elif self.position == 2:
            self.position[1] += -self.sheep_move_dist
        else:
            self.position[0] += self.sheep_move_dist
        logging.info('Owca nr ' + str(self.id) + ' przemieściła się z punktu: (' + str(old_pos[0]) + '; ' + str(old_pos[1]) + ') do punktu (' + str(self.position[0]) + '; ' + str(self.position[1]) + ')')
