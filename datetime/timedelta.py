"""
you can create a timedelta object representing a certain duration of time using the datetime.timedelta() function.
"""
import datetime
dt = datetime.datetime(2023, 3, 8, 12, 0, 0) # create a datetime object representing March 8, 2023 at noon
delta = datetime.timedelta(hours=2, minutes=15)
result = dt + delta
print(result)
# add the timedelta object to the datetime object to get a new datetime object
