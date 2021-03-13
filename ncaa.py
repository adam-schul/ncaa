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
avg_list = []

limit = 15

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

for p in range(1, 35, 5):
    low_limit = p
    high_limit = p + 5
    high_limt = high_limit - 1
    for i in range(1985, 2008):
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
                # If it's a blowout, save the information to another list
                if (difference >= low_limit) and (difference <= high_limit):
                    blowout.append([nineteen[i][0], difference, nineteen[i][2]])
                else:
                    pass
            else:
                pass

        numwon = 0

        # Calculate how many of the blowout winners won in the next round.
        for d in range(len(blowout)):
            for i in range(len(nineteen)):

                # If in the second round, the winning team matches a team that won a blowout
                if (nineteen[i][1] == '138' or nineteen[i][1] == '139') and blowout[d][2] == nineteen[i][2]:
                    numwon = numwon + 1
                else:
                    pass

        # Calculate the proportion of blowout winners that won in the next round.
        try:
            propwon = (numwon) / (len(blowout))
            sum_prop.append(propwon)

        except ZeroDivisionError:
            pass

    glass = 0
    for i in range(len(sum_prop)):
        glass = glass + sum_prop[i]

    avg = glass / len(sum_prop)
    avg_list.append(avg)

    print('Avg prop. of teams who won second game if won first game with a lead '
          'between ' + str(low_limit) + ' and ' + str(high_limt) + ': ' + str(truncate((avg), 5)))

