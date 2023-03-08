"""
Getting the current local date and creating date objects
"""

from datetime_3 import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)



