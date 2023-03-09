"""
How can you determine if a year is a leap year using the calendar module in Python?
"""

import calendar
import datetime
date_obj = datetime.date(2023, 3, 8)
week_num = calendar.Calendar().weeknumber(date_obj)
print(calendar)