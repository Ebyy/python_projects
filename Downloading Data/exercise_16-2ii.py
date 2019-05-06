import csv

import matplotlib.pyplot as plt

from datetime import datetime


filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get temperatures
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the data
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, c='green', alpha=0.7)
plt.plot(dates, lows, c='red', alpha=0.7)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot
title = "Daily high low temperatures - 2014 \nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.ylim(10, 120)

plt.show()
