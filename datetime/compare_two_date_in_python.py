from datetime import datetime

dt1 = datetime(2021, 10, 11, 10, 10, 10)
dt2 = datetime(2021, 11, 11, 10, 10, 10)

if dt1 > dt2:
    print(f"dt1 date is greater than dt2 by this many days {dt1-dt2}")
else:
    print(f"dt2 is greater than dt1 by this many days {dt2-dt1}")


