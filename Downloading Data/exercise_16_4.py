import csv

import matplotlib.pyplot as plt

from datetime import datetime


filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get rainfall data
    dates, rainfall, totals = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rain = float(row[19])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            rainfall.append(rain)
            if totals:
                totals.append(totals[-1] + rain)
            else:
                totals.append(rain)

# Plot data
fig = plt.figure(figsize=(10, 6))
plt.plot(dates, rainfall, c='blue', alpha=0.7)
plt.fill_between(dates, rainfall, facecolor='red', alpha=0.2)

plt.plot(dates,totals,c='blue',alpha=0.4)
plt.fill_between(dates,totals,facecolor='blue',alpha=0.1)

# Format plot
title = "Daily Rainfall amounts and Cumulative amount - 2014  \nSitka, AK"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Rainfall (in)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
