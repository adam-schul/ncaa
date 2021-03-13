
import numpy as np
import matplotlib.pyplot as plt
import sys, csv
from matplotlib.pyplot import xkcd




# Read the data from the csv file and put it into a variable called "data"
with open('NCAATourneyCompactResults.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# Sort the data into the more specific lists

sum_prop = []

limit = 15

for i in range(1985, 2017):
    # Create empty lists for data
    blowout = []
    nineteen = []

    # Set the year as a variable
    year = str(i)

    # Isolate data in specific year
    for i in range(len(data)):
        if data[i][0] == year:
            nineteen.append(data[i])
        else:
            pass

    # Isolate blowouts in first round within the year. Save how much they won by, the year, and the code of the winner.
    for i in range(len(nineteen)):
        if i == 0:
            pass
        elif data[i][1] == '136' or data[i] == '137':
            difference = int(data[i][3]) - int(nineteen[i][5])
            if difference > limit:
                blowout.append([nineteen[i][0], difference, nineteen[i][2]])
            else:
                pass
        else:
            pass

    numwon = 0

    # Calculate how many of the blowout winners won in the next round.
    for d in range(len(blowout)):
        for i in range(len(nineteen)):
           if (nineteen[i][1] == '138' or nineteen[i][1] == '139') and blowout[d][2] == nineteen[i][2]:
                numwon = numwon + 1
           else:
               pass

    # Calculate the proportion of blowout winners that won in the next round.
    try:
        propwon = float(float(numwon) / float(len(blowout)))
        sum_prop.append(propwon)

    except ZeroDivisionError:
        print('There were no blowouts in' + year + '.')

glass = sum(sum_prop)
avg = glass/len(sum_prop)

print('Average proportion: ' + str(avg))

