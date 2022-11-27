import datetime
from datetime import timedelta

DateInput = input().split('-')

dt = datetime.datetime(int(DateInput[2]), int(DateInput[1]), int(DateInput[0]))

if (dt.weekday() == 0):
    if int(dt.month) < 10:
        t = "0" + str(dt.month)
    print("{}-{}-{}".format(dt.day, t, dt.year))
else:
    tmp = dt - timedelta(days=dt.weekday())
    if int(tmp.month) < 10:
        t = "0" + str(tmp.month)
    print("{}-{}-{}".format(tmp.day, t, tmp.year))