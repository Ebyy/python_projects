import csv

import matplotlib.pyplot as plt

from datetime import datetime


filename = 'sitka_weather_2014.csv'
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
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data
fig = plt.figure(figsize=(10,6))
plt.plot(dates,highs,c='green',alpha=0.7)
plt.plot(dates, lows, c='red',alpha=0.7)

plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# Format plot
plt.title("Daily high and low temperatures - 2014 \nSitka, Alaska", fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
# Set limit for y axis
plt.ylim(10,80)

plt.show()