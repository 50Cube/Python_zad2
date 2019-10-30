from Zadanie2.wolf import *
from Zadanie2.JSONfile import *
from Zadanie2.CSVfile import *
import os
from os import path


def simulate(rounds, sheep_amount, sheep_limit, wolf_distance, sheep_distance, json_file, csv_file):
    if path.exists(json_file):
        os.remove(json_file)
    if path.exists(csv_file):
        os.remove(csv_file)
    sheeps = []
    wolf = Wolf(wolf_distance)

    data = {'rounds': []}
    with open(json_file, 'a') as outfile:
        json.dump(data, outfile, indent=1)

    for i in range(sheep_amount):
        sheeps.append(Sheep(i, sheep_limit, sheep_distance))

    for i in range(rounds):
        print("Numer tury: " + str(i+1))
        print("Liczba owiec: " + str(len(sheeps)))
        wolf.print_wolf()
        if len(sheeps) == 0:
            print("Wilk zjadl wszystkie owce")
            break
        for j in range(len(sheeps)):
            sheeps[j].move_sheep()
            # sheeps[j].print_sheep()
        print("")
        saveToJSON(json_file, i, wolf, sheeps, sheep_amount, data)
        saveToCSV(csv_file, i, len(sheeps))
        tmp_sheep, tmp_dist = wolf.check_distance(sheeps)
        wolf.move(tmp_sheep, tmp_dist, sheeps)


if __name__ == "__main__":
    simulate(50, 15, 10.0, 1.0, 0.5, 'pos.json', 'alive.csv')
