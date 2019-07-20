import time
import datetime

def substraiHoras(time1, time2):
    time1 = time.strptime(time1, '%H:%M:%S')
    time2 = time.strptime(time2, '%H:%M:%S')

    dif = abs(time1.tm_hour * 3600 - time2.tm_hour * 3600)
    dif += abs(time1.tm_min * 60 - time2.tm_min * 60)
    dif += abs(time1.tm_sec - time2.tm_sec)

    print (datetime.timedelta(seconds=dif))

time1 = "01:05:23" 
time2 = "20:59:50"

substraiHoras(time1, time2)