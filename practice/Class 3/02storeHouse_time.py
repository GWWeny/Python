import time
# 获取当前时间戳，即计算机内部时间值，浮点数
print(time.time())
# 获取当前时间并以易读方式表示，返回字符串
print(time.ctime())
# 是把日期和时间转换为UTC时间的函数
# 默认获取当前时间，表示为计算机可处理的时间
# 格式
print(time.gmtime())
# strftime(tpl,ts)
# tpl是格式化模板字符串，用来定义输出效果
# ts是计算机内部时间类型变量
# %Y  年份     %a  星期缩写
# %m  月份     %H  小时(24h制)
# %B  月份名称     %1  小时(12h制)
# %b  月份名称缩写     %p  上下午
# %d  日期     %M  分钟
# %A  星期     %S  秒
t=time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",t))
# strptime(str.tpl)
# str是字符串形式的时间值
# tpl是格式化模板字符串，用来定义输出效果
timestr="2018-11-13 14:30:30"
t=time.strptime(timestr,"%Y-%m-%d %H:%M:%S")
print(t)
# 单位秒，可以是浮点数
def wait():
    time.sleeo(3.3)
wait()