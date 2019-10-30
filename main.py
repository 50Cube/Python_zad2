from wolf import *
from JSONfile import *
from CSVfile import *
import os
from os import path
import argparse


def simulate(rounds, sheep_amount, sheep_limit, wolf_distance, sheep_distance, json_file, csv_file, wait=False):
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
        if wait:
            input()
        saveToJSON(json_file, i, wolf, sheeps, sheep_amount, data)
        saveToCSV(csv_file, i, len(sheeps))
        tmp_sheep, tmp_dist = wolf.check_distance(sheeps)
        wolf.move(tmp_sheep, tmp_dist, sheeps)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", metavar="FILE")
    parser.add_argument("-d", "--dir", metavar="DIR")
    parser.add_argument("-l", "--log", metavar="LEVEL")
    parser.add_argument("-r", "--rounds", metavar="NUM", type=int)
    parser.add_argument("-s", "--sheep", metavar="NUM", type=int)
    parser.add_argument("-w", "--wait", action="store_true")
    args = parser.parse_args()
    if args.config:
        print()
    elif args.dir:
        print()
    elif args.log:
        print()
    elif args.rounds:
        simulate(args.rounds, 15, 10.0, 1.0, 0.5, 'pos.json', 'alive.csv')
    elif args.sheep:
        simulate(50, args.sheep, 10.0, 1.0, 0.5, 'pos.json', 'alive.csv')
    elif args.wait:
        simulate(50, 15, 10.0, 1.0, 0.5, 'pos.json', 'alive.csv', True)
    else:
        simulate(50, 15, 10.0, 1.0, 0.5, 'pos.json', 'alive.csv')
