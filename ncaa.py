import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
from matplotlib.pyplot import xkcd

# Read the data from the csv file and put it into a variable called "data"
with open('NCAATourneyCompactResults.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# Sort the data into the more specific lists

sum_prop = []
avg_list = []


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


for p in range(1, 35, 5):
    low_limit = p
    high_limit = p + 5
    high_lmt = high_limit - 1
    for i in range(1985, 2008):
        # Create empty lists for data
        blowout = []
        nineteen = []

        # Set the year as a variable
        year = str(i)

        # Isolate data in specific year
        for q in range(len(data)):
            if data[q][0] == year:
                nineteen.append(data[q])
            else:
                pass

        # Isolate blowouts in first round within the year. Save how much they won by, the year,
        # and the code of the winner.
        for r in range(len(nineteen)):
            if r == 0:
                pass
            elif data[r][1] == '136' or data[r] == '137':
                difference = int(data[r][3]) - int(nineteen[r][5])
                # If it's a blowout, save the information to another list
                if (difference >= low_limit) and (difference <= high_limit):
                    blowout.append([nineteen[r][0], difference, nineteen[r][2]])
                else:
                    pass
            else:
                pass

        numWon = 0

        # Calculate how many of the blowout winners won in the next round.
        for d in range(len(blowout)):
            for w in range(len(nineteen)):

                # If in the second round, the winning team matches a team that won a blowout
                if (nineteen[w][1] == '138' or nineteen[w][1] == '139') and blowout[d][2] == nineteen[w][2]:
                    numWon = numWon + 1
                else:
                    pass

        # Calculate the proportion of blowout winners that won in the next round.
        try:
            propWon = numWon / (len(blowout))
            sum_prop.append(propWon)

        except ZeroDivisionError:
            pass

    glass = 0
    for i in range(len(sum_prop)):
        glass = glass + sum_prop[i]

    avg = glass / len(sum_prop)
    avg_list.append(avg)

    print('Avg prop. of teams who won second game if won first game with a lead '
          'between ' + str(low_limit) + ' and ' + str(high_lmt) + ': ' + str(truncate(avg, 5)))
