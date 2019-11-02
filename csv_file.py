import csv
import logging


def save_to_csv(file, i, amount):
    logging.debug('save_to_csv(file=' + file +
                  ', i=' + str(i) +
                  ', amount=' + str(amount) + ')')
    with open(file, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')

        writer.writerow([i+1, amount])
