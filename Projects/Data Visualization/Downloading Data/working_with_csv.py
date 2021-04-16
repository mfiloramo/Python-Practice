import csv
from matplotlib import pyplot
from datetime import datetime


# Get dates and high, and low temperatures from file.
filename = "Scrap Files/death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# List the scores. (I had to modify the way that it appended to the list because
# the first value was a date. Then I had to make sure that ints were being added
# to the list. I probably could've kept it with floats, but I wanted to be neat.)
    dates, highs, lows = [], [], []
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


# Plot data.
    fig = pyplot.figure(dpi=128, figsize=(10, 6))
    pyplot.plot(dates, highs, c="red", alpha=0.5)
    pyplot.plot(dates, lows, c="blue", alpha=0.5)
    pyplot.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
    pyplot.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
    pyplot.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    pyplot.ylabel("Temperature (F)", fontsize=16)
    pyplot.tick_params(axis="both", which="major", labelsize=15)
    pyplot.ylim([0, 120])

    pyplot.show()

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

