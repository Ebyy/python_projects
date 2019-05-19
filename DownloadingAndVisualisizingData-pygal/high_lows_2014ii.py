import csv

from matplotlib import pyplot as plt

from datetime import datetime

# Get dates, high, and low temperatures from files
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

# Plot data
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, highs, c='green',alpha=0.5)
plt.plot(dates, lows, c='red',alpha=0.5)

# To fill or shade the space in between the two plots
# *alpha controls color transparency with range from 0-1
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# Format the plot
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
