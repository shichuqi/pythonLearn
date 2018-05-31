'''
定义一个学生类，用来形容学生
'''

# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
mingyue = Student()


# 定义一个类，用来描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name    =   None
    age     =   18
    course  =   "Python"

    # 需要注意
    # 方法的缩进层级
    # 系统默认有一个self参数
    def doHomework(self):
        print("I\'m doing Homework")
        # 推荐在函数末尾使用return 语句
        return None

# 实例化一个对象
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
print(yueyue.course)

# 需要注意的是  此处没有传入参数
yueyue.doHomework()







