from datetime import datetime
import secrets
import string
import csv
import os
from constants import CSV_HEADER, CSV_DATA


def create_csv_files(number):
    """
    Create csv sample files.
    """

    for i in range(number):
        random_number = ''.join(secrets.choice(string.digits) for _ in range(5))
        filename = str(datetime.now().date()) + '-' + str(random_number)
        write_csv_file(filename)
    print('CSV files created successfully')


def write_csv_file(filename):
    """
    Write csv file function.

    :param filename: csv file name.
    :return: create csv sample files in "files" directory.
    """
    if not os.path.isdir('files/'):  # create directory if directory does not exist.
        os.mkdir('files')

    with open(f'files/{filename}.csv', 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER)
        writer.writerows(CSV_DATA)
