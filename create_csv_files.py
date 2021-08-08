from datetime import datetime
import csv
from constants import NUMBER_OF_INITIAL_FILES, NUMBER_OF_NEW_FILES, CSV_HEADER, CSV_DATA


def create_csv_files(state):
    """
    Create csv sample files.

    :param state: Specify where you are at the stage of creating the file: "initial" or "new".
    :return: create csv sample files in "files" directory.
    """

    if state == 'initial':
        for i in range(NUMBER_OF_INITIAL_FILES):
            filename = str(datetime.now().date()) + '-' + str(i + 1)
            write_csv_file(filename)

    else:
        for i in range(NUMBER_OF_NEW_FILES):
            filename = str(datetime.now().date()) + '-' + str(NUMBER_OF_INITIAL_FILES + i + 1)
            write_csv_file(filename)
    print('CSV files created successfully')


def write_csv_file(filename):
    """
    Write csv file function.

    :param filename: csv file name.
    :return: create csv sample files in "files" directory.
    """

    with open(f'files/{filename}.csv', 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER)
        writer.writerows(CSV_DATA)
