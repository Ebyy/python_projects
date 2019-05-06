import csv

import matplotlib.pyplot as plt

from datetime import datetime


def get_weather_data(filename, dates, highs, lows):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, "missing data")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# Plot Sitka data
fig = plt.figure(figsize=(10, 6))
dates, highs, lows = [], [], []
get_weather_data('sitka_weather_2014.csv', dates, highs, lows)
plt.plot(dates, highs, c='red', alpha=0.4)
plt.plot(dates, lows, c='blue', alpha=0.4)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.05)

# Plot Death Valley data
dates, highs, lows = [], [], []
get_weather_data('death_valley_2014.csv', dates, highs, lows)
plt.plot(dates, highs, c='red', alpha=0.8)
plt.plot(dates, lows, c='blue', alpha=0.8)
plt.fill_between(dates, highs, lows, facecolor='pink', alpha=0.1)

# Format plot
title = "Daily hig low temperatures -2014 \nDeath Valley, CA and Sitka,AK"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperatures (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.ylim(10, 120)

plt.show()
