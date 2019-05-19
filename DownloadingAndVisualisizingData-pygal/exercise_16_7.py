import csv

import matplotlib.pyplot as plt

from datetime import datetime


filename = 'global_pop_growth.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, pop_growths = [], []

    for index, column in enumerate(header_row):
        print(index, column)