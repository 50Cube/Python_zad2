from Zadanie2.sheep import *
import math


class Wolf:
    def __init__(self, distance):
        self.position = [0.0, 0.0]
        self.wolf_move_dist = distance

    def print_wolf(self):
        print("Wilk znajduje sie na pozycji [" + "%0.3f" % self.position[0] + ", " + "%0.3f" % self.position[1] + "]")

    def check_distance(self, sheeps):
        closest_sheep = sheeps[0]
        closest_sheep_distance = math.sqrt((sheeps[0].position[0] - self.position[0])**2 + (sheeps[0].position[1] - self.position[1])**2)
        for i in range(1, len(sheeps)):
            if math.sqrt((sheeps[i].position[0] - self.position[0])**2 + (sheeps[i].position[1] - self.position[1])**2) < closest_sheep_distance:
                closest_sheep = sheeps[i]
                closest_sheep_distance = math.sqrt((sheeps[i].position[0] - self.position[0])**2 + (sheeps[i].position[1] - self.position[1])**2)
            #print(closest_sheep_distance)
            #closest_sheep.print_sheep()
        return closest_sheep, closest_sheep_distance

    def move(self, sheep, distance, sheeps):
        if distance < self.wolf_move_dist:
            print("Wilk zjadl owce nr " + str(sheep.id+1) + " :(")
            print("")
            self.position[0] = sheep.position[0]
            self.position[1] = sheep.position[1]
            sheeps.remove(sheep)
        else:
            #print("gonie owce nr " + str(sheep.id+1))
            #print("")
            vector = [0.0, 0.0]
            vector[0] = sheep.position[0] - self.position[0]
            vector[1] = sheep.position[1] - self.position[1]
            vector_length = math.sqrt(vector[0]**2 + vector[1]**2)
            self.position[0] += (vector[0]/vector_length)*self.wolf_move_dist
            self.position[1] += (vector[1] / vector_length)*self.wolf_move_dist
