"""
Open csv
"""
import csv

words_csv = []

def open_csv():
    """
    Open csv
    """
    with open('words.csv', 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            words_csv.append(row)
        return words_csv
    