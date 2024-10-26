import time
import datetime
from datetime import date
from datetime import timedelta
# 使用下面的方法直接计算今天是今年的第几天
print(time.gmtime().tm_yday)
print(datetime.date.today().timetuple().tm_yday)
print(datetime.date(2019,11,5).timetuple().tm_yday)
print("--------------------")
# 使用datetime模块提供的功能来计算今年的第几天
today=datetime.date.today()
print(today)
firstDay=datetime.date(today.year,1,1)
print(firstDay)
daysDelta=today-firstDay+datetime.timedelta(days=1)
print(daysDelta)
print("--------------------")
# datetime还提供了其他功能
now =datetime.datetime.now()
print(now)
# 替换日期时间中的秒
print(now.replace(second=30))
# 计算5天后的日期时间
print(now+datetime.timedelta(days=5))
# 计算5周前的日期时间
print(now+datetime.timedelta(weeks=-5))
# 差35秒两天前
print(now+datetime.timedelta(days=-2,seconds=-35))
# 差35秒两周前
print(now+datetime.timedelta(weeks=-2,seconds=-35))
print("--------------------")
# 计算两个日期之间相差多少天
def daysBetween(year1,month1,day1,year2,month2,day2):
    return (date(year1,month1,day1)-date(year2,month2,day2)).days
print(daysBetween(2019,11,5,2019,11,1))
print(daysBetween(2019,11,5,2019,11,6))
print("--------------------")
# 计算某年第n个周五是几月几号。
def getDate(year,weeks,weekday):
    start = date(year,1,1)
    for i in range(7):
        if start.isoweekday()==weekday:
            break
        start = start +timedelta(days=1)
    return start + timedelta(weeks=weeks-1)
print(getDate(2019,22,5))