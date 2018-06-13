# calendar
import calendar

cal = calendar.calendar(2018,w=0,l=0,c=0)
print(cal)



# isleap:判断某一年是否是闰年
print(calendar.isleap(2018))

# leapdays:获取指定年份之间的闰年的个数,包含左不包含右
print(calendar.leapdays(2003,2004))
print(help(calendar.leapdays))

# month() 获取某个月的日历字符串
# 格式：calendar.month(年，月)
# 返回值：月日历的字符串
print(calendar.month(2017,2))

# monthrange() 获取一个月的周几开始即和天数
# 格式：calendar.monthrange(年，月)
# 返回值：元组（周几开始，总天数）
# 注意：周默认0-6表示周一到周天
m = calendar.monthcalendar(2017,2)
print(m)

# prical:print calendar 直接打印日历
# calendar.prcal(2018)
calendar.prcal(2018)

# weekday() 获取周几
# 返回值： 0-6 周一到周日
print(calendar.weekday(2018,6,13))