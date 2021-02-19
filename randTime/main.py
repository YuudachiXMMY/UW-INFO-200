import datetime
import random as r

def rand(n):
    while n != 0:
        year = 2021
        month = 2
        day = r.randint(1, 16)
        hour = r.randint(0, 23)
        min = r.randint(0, 59)
        second = r.randint(0, 59)
        tmp = r.randint(100000, 199999)

        c = datetime.datetime(year, month, day, hour, min, second, tmp)
        res = c.strftime("%m/%d/%Y %H:%M:%S")
        print(res)
        n -= 1

rand(50)