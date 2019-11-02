import json
import logging


def save_to_json(file, i, wolf, sheeps, sheep_amount, data):
    logging.debug('save_to_json(file=' + file +
                  ', i=' + str(i) +
                  ', wolf=' + str(wolf) +
                  ', sheeps=' + str(sheeps) +
                  ', sheep_amount=' + str(sheep_amount) +
                  # ', data=' + str(data) +
                  ')')
    tmp = []
    for j in range(0, sheep_amount):
        tmp += [None]

    for j in range(0, len(sheeps)):
        tmp[sheeps[j].id] = sheeps[j].position

    data['rounds'].append({
        'round_no': i+1,
        'wolf_pos': wolf.position,
        'sheep_pos': tmp
    })

    with open(file, 'w') as outfile:
        json.dump(data, outfile, indent=1)
