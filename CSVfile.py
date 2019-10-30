import csv


def saveToCSV(file, i, amount):
    with open(file, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')

        writer.writerow([i+1, amount])
