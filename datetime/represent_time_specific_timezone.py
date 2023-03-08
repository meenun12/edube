"""
How can you create a datetime object representing a specific time in a specific time zone in Python?
"""

from datetime import datetime
import pytz

tz = pytz.timezone("America/New_York")

dt = datetime(2022, 11, 10, tzinfo=tz)

print(dt)




