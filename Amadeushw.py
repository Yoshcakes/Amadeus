# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

#Reading the data and specifying the number of rows for faster import
nrowssearch = 20390198
nrowsbookings = 10000011
searches = pd.read_csv("searches.csv", sep='^', nrows = 50000)
bookings = pd.read_csv("bookings.csv", sep='^', nrows = 10000)

#Taking a look at the data before diving in
print searches.head()
print bookings.head()

# Question 1
print 'The number of row in the searches dataframe is ', len(searches)
print 'The number of row in the bookings dataframe is ', len(bookings)

# Question 2
answer = bookings.groupby('arr_port').sum().sort('pax', ascending = False).head(10)
print 'The top 10 arrival airports in term of number of passengers are \n', answer[['pax']]

with open('test.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(answer[['pax']])
    fp.close()


# Question 3
# Adding two new variables called month and year for easy
searches['month'] = pd.DatetimeIndex(searches['Date']).month
searches['year'] = pd.DatetimeIndex(searches['Date']).year

# Creating empty list to be used in the histograms
Mal = [0]*12
Mad = [0]*12
Bar = [0]*12

# Filling in the lists
for i in xrange(len(searches)):
    if searches['year'][i] == 2013 and searches['Destination'][i] == 'AGP':
        Mal[searches['month'][i] - 1] += 1
    if searches['year'][i] == 2013 and searches['Destination'][i] == 'MAD':
        Mad[searches['month'][i] - 1] += 1
    if searches['year'][i] == 2013 and searches['Destination'][i] == 'BCN':
        Bar[searches['month'][i] - 1] += 1

# Creating the histogram    
ind = np.arange(len(Mal))  # the x locations for the groups
width = 0.33               # the width of each bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, Mal, width, color='r')
rects2 = ax.bar(ind + width, Mad, width, color='b')
rects3 = ax.bar(ind + 2*width, Bar, width, color='g')

# add some text for labels, title and axes ticks
ax.set_ylabel('Number of searches')
ax.set_title('Number of searches by month for the airports of Malaga, Madrid and Barcelona in 2013')
ax.set_xticks(ind + 1.5*width)
ax.set_xticklabels( ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec') )

#Add the legend
ax.legend( (rects1[0], rects2[0], rects3[0]), ('Malaga Airport', 'Madrid Airport', 'Barcelona Airport') )

plt.show()

# We could have probably approached this question differently by first creating a subset
# of the searches for the year 2013 and then grouping the searches by month and counting
# the number of searches for each airport.

# Bonus question 1
