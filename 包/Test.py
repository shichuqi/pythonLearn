import p01
import importlib

stu = p01.Student('jack',23)
print(stu.name)
stu.say()
p01.sayHello()


# 使用importlib包可以实现导入以数字开头的模块名
modu = importlib.import_module('01')

student = modu.Student()
student.say()
