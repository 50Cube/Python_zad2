import argparse
import configparser
import os
import sys
from csv_file import *
from json_file import *
from wolf import *


def simulate(rounds,
             sheep_amount,
             sheep_limit,
             wolf_distance,
             sheep_distance,
             json_file,
             csv_file,
             directory=".",
             wait=False):
    logging.debug('main.simulate(rounds=' + str(rounds) +
                  ', sheep_amount=' + str(sheep_amount) +
                  ', sheep_limit=' + str(sheep_limit) +
                  ', wolf_distance=' + str(wolf_distance) +
                  ', sheep_distance=' + str(sheep_distance) +
                  ', json_file=' + json_file +
                  ', csv_file=' + csv_file +
                  ', directory=' + directory +
                  ', wait=' + str(wait) + ')')
    if directory != '.' and not os.path.exists(directory):
        os.mkdir(directory)
    if os.path.exists(directory + '/' + json_file):
        os.remove(directory + '/' + json_file)
    if os.path.exists(directory + '/' + csv_file):
        os.remove(directory + '/' + csv_file)
    sheeps = []
    wolf = Wolf(wolf_distance)

    data = {'rounds': []}
    with open(json_file, 'a') as outfile:
        json.dump(data, outfile, indent=1)

    for i in range(sheep_amount):
        sheeps.append(Sheep(i, sheep_limit, sheep_distance))

    for i in range(rounds):
        print('Numer tury: ' + str(i+1))
        print('Liczba owiec: ' + str(len(sheeps)))
        wolf.print_wolf()
        if len(sheeps) == 0:
            print('Wilk zjadł wszystkie owce')
            break
        for j in range(len(sheeps)):
            sheeps[j].move_sheep()
            # sheeps[j].print_sheep()
        print()
        if wait:
            input()
        save_to_json(directory + '/' + json_file, i, wolf, sheeps, sheep_amount, data)
        save_to_csv(directory + '/' + csv_file, i, len(sheeps))
        tmp_sheep, tmp_dist = wolf.check_distance(sheeps)
        wolf.move(tmp_sheep, tmp_dist, sheeps)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', metavar='FILE')
    parser.add_argument('-d', '--dir', metavar='DIR')
    parser.add_argument('-l', '--log', metavar='LEVEL', type=int)
    parser.add_argument('-r', '--rounds', metavar='NUM', type=int)
    parser.add_argument('-s', '--sheep', metavar='NUM', type=int)
    parser.add_argument('-w', '--wait', action='store_true')
    args = parser.parse_args()
    if not len(sys.argv) > 1:
        simulate(50, 15, 10.0, 1.0, 0.5, 'pos.json', 'alive.csv')
    else:
        init_pos_limit = 10.0
        sheep_move_dist = 0.5
        wolf_move_dist = 1.0
        d = '.'
        lo = 0
        r = 50
        s = 15
        w = False
        if args.config:
            config = configparser.ConfigParser()
            config.read(args.config)
            init_pos_limit = float(config['Terrain']['InitPosLimit'])
            sheep_move_dist = float(config['Movement']['SheepMoveDist'])
            if sheep_move_dist <= 0:
                msg = 'Długość odcinka pokonywanego w trakcie jednej tury przez owce musi być liczbą dodatnią'
                logging.critical(msg)
                raise ValueError(msg)
            wolf_move_dist = float(config['Movement']['WolfMoveDist'])
            if wolf_move_dist <= 0:
                msg = 'Długość odcinka pokonywanego w trakcie jednej tury przez wilka musi być liczbą dodatnią'
                logging.critical(msg)
                raise ValueError(msg)
        if args.dir:
            d = args.dir
        if args.log:
            lo = args.log
            if d != '.' and not os.path.exists(d):
                os.mkdir(d)
            logging.basicConfig(filename=d+'/chase.log', filemode='w', level=lo)
        if args.rounds:
            r = args.rounds
            if r <= 0:
                msg = 'Liczba tur musi być liczbą całkowitą większą od 0'
                logging.critical(msg)
                raise ValueError(msg)
        if args.sheep:
            s = args.sheep
            if s <= 0:
                msg = 'Liczba owiec musi być liczbą całkowitą większą od 0'
                logging.critical(msg)
                raise ValueError(msg)
        if args.wait:
            w = True
        simulate(r, s, init_pos_limit, wolf_move_dist, sheep_move_dist, 'pos.json', 'alive.csv', d, w)
