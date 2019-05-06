import csv

import matplotlib.pyplot as plt

from datetime import datetime


filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get the data
    dates, rains = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rain = float(row[19])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            rains.append(rain)

# Plot data
fig = plt.figure(figsize=(10,6))
plt.plot(dates, rains, c='blue')

# Format plot
title = "Daily rainfall in Death valley - 2014"
plt.title(title,fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)


plt.show()