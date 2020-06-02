"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

#if no arguments provided print current month calendar

#if one argument passed, print the calendar for the corresponding month for the current year

#if two arguments passed, print the calendar for the month and year provided (ie first argument is month, second argument is year)

#else print an eror message informing the user of their invalid input

n = len(sys.argv)
now = datetime.now()

# year = int(now.strftime("%Y"))
# month = int(now.strftime("%m"))

# print(n)

# print(sys.argv[1])

if n == 1:
  year = int(now.strftime("%Y"))
  month = int(now.strftime("%m"))
  print(calendar.month(year, month))
elif n == 2:
  year = int(now.strftime("%Y"))
  month = int(sys.argv[1])
  print(calendar.month(year, month))
elif n == 3:
  year = int(sys.argv[2])
  month = int(sys.argv[1])
  print(calendar.month(year, month))
else:
  print("""
    Error: 14_cal.py requires 0-2 arguements.
    0 arguments will print the current months calendar.
    1 argument will print the respective months calendar for this year.
    2 arguments will print the calendar for the provided month and year.""")
