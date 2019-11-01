import csv
import logging


def saveToCSV(file, i, amount):
    logging.debug('saveToCSV(file=' + file +
                  ', i=' + str(i) +
                  ', amount=' + str(amount) + ')')
    with open(file, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')

        writer.writerow([i+1, amount])
