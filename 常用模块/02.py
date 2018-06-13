# time 时间戳
import time

# timezone:当前时区和UTC时间相差的秒数，在没有夏令时的间隔

print(time.timezone)

# time() 得到时间戳

print(time.time())

# localtime:得到当前时间的时间结构
t = time.localtime()
print(t)

# asctime() :返回元组的正常字符串化之后的时间格式 Wed Jun 13 22:28:05 2018
print(time.asctime(t))

# ctime :获取字符串化的当前时间
print(time.ctime())

# mktime() ：使用时间元组获取对应的时间戳
# 返回值：浮点数时间戳

lt = time.localtime()
ts = time.mktime(lt)
print(type(ts))
print(ts)

# clock : 获取CPU时间，3.0-3.3版本直接使用，3.6调用有问题


# sleep :   使程序进入睡眠，n秒后继续

# for i in range(10):
#     print(i)
#     time.sleep(1)


# strftime：将时间元组转化为自定义的自负串格式

# 具体参数 查看教程项目

# 常用表示  2018-5-14 00:00:00
t = time.localtime()
ft = time.strftime("%Y-%m-%d %H:%M:%S")
print(ft)

# datetime ： 常见属性

import  datetime
dt = datetime.date(2018,3,26)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)

# datetime.datetime
# 常用类方法：today,now,utcnow,fromtimestamp(从时间戳中返回本地时间)
from datetime import datetime,timedelta
dt = datetime(2018,3,26)
print(dt.today())
print(dt.now())


# 当前时间加上时间间隔后，把时间格式化输出
t1 = datetime.now()
print(type(t1))
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
tt = timedelta(hours=1)
print(type(tt))


# timeit :时间测量工具  (具体看教程项目)

def p():
    time.sleep(1)

t1 = time.time()
p()
print(time.time() - t1)

import timeit
t1 = timeit.timeit(stmt='[i for i in range(1000)]',number=100000)

print(t1)


