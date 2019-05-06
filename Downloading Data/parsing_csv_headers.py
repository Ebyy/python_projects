import csv


filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row) can be substituted for a more detailed outline as given below.

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #to print the values in a particular column as strings
    # highs = []
    # for row in reader:
        # highs.append(row[1])
    # print(highs)

# or as integers
    temp_highs = []
    for row in reader:
        high = int(row[1])
        temp_highs.append(high)
    print(temp_highs)
