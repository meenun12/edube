"""
How can you calculate the number of days between two datetime objects in Python?
"""

from datetime import date

d1 = date(2021, 10, 5)
d1.strftime("%Y/%M/%D")
print(d1)


