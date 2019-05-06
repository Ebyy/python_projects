import csv

import matplotlib.pyplot as plt

from datetime import datetime


# Get temperatures from file

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
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the data

fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, c='blue', alpha=0.7)
plt.plot(dates, lows, c='red', alpha=0.7)

plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

# Format plots
plt.title("Daily high low temperatures - 2014 in Death Valley, CA", fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()
