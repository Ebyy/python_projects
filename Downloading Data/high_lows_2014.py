import csv

from datetime import  datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0],'%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

# Plot results
fig = plt.figure(figsize=(11,6))
plt.plot(dates,highs,c='red')

# Format plot
plt.title('Daily high temperatures - 2014', fontsize=20)
plt.xlabel('',fontsize =14)
fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()