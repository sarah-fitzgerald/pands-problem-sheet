#This program outputs whether today is a weekday or not
#Author: Sarah Fitzgerald

#https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

#Imports date object: https://docs.python.org/3/library/datetime.html#datetime.date.weekday
import datetime

#Returns the day of the week as an integer
day = datetime.datetime.today().weekday()

#Day 0-4 is a weekday
if day < 5:
    print ("Yes, unfortunately today is a weekday")

#Day 5 and 6 is a weekend
else:
    print ("It is the weekend, yay!")

#Print out a string depending on the day of the week
print (day)