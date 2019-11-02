import logging
import random


class Sheep:
    def __init__(self, id, limit, distance):
        logging.debug('sheep.__init__(id={0}, limit={1} distance={2})'.format(str(id), str(limit), '%0.3f' % distance))
        self.id = id
        self.init_pos_limit = limit
        self.position = [random.uniform(-self.init_pos_limit, self.init_pos_limit),
                         random.uniform(-self.init_pos_limit, self.init_pos_limit)]
        logging.info('Ustalenie pozycji poczatkowej owcy nr {0}: ({1}; {2})'.format(str(id), '%0.3f' % self.position[0],
                                                                                    '%0.3f' % self.position[1]))
        self.sheep_move_dist = distance

    def print_sheep(self):
        logging.debug('sheep.print_sheep()')
        print('Owca nr {0} znajduje sie na pozycji {1}'.format(str(self.id + 1), str(self.position)))

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
        logging.info('Owca nr {0} przemieściła się z punktu: '
                     '({1}; {2}) do punktu ({3}; {4})'.format(str(self.id),
                                                              '%0.3f' % old_pos[0],
                                                              '%0.3f' % old_pos[1],
                                                              '%0.3f' % self.position[0],
                                                              '%0.3f' % self.position[1]))

    def __str__(self):
        return 'Sheep(id: {0}, position: ({1}; {2}))'.format(str(self.id),
                                                             '%0.3f' % self.position[0],
                                                             '%0.3f' % self.position[1])

    def __repr__(self):
        return self.__str__()
