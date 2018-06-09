# 变量的三种用法

class A():
    def __init__(self):
        self.name = 'aaa'
        self.age = 18
    # 此功能，是对类变量进行读取操作
    def fget(self):
        print('我被读取了')
        return self.name
    # 写操作
    def fset(self,name):
        print("我被写入")
        self.name = 'dvxvfwea'+name
    # 删除
    def fdel(self):
        pass

    name2 = property(fget,fset,fdel,"This is a example!")

a = A()
# 属性的三种用法（赋值，读取，删除）
print(a.name)
# del a.name

print(a.name2)


# 抽象
class Animel():
    def sayHello(self):
        pass

class Dog(Animel):
    def sayHello(self):
        print('wenyixia')

class Person(Animel):
    def sayHello(self):
        print('kiss me')

d = Dog()
d.sayHello()

p = Person()
p.sayHello()


print('%'*20)

# 抽象类的实现

import abc
# 声明一个类并且指定当前类的元类
class Human(metaclass = abc.ABCMeta):

    # 定一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类的抽象放法
    @abc.abstractclassmethod
    def drink(cls):
        pass

    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

# 自己组装一个类

from types import MethodType
class Zlass():
    pass

def say(self):
    print('saying...')

def talk(self):
    print('talking...')

say(9)

a =Zlass()
a.say = MethodType(say,Zlass)
a.say()
# help(MethodType)
#
# help(type)

print(type(9))

#利用type创建一个类
Z = type('ZName',(object,),{'class_say':say,'class_talk':talk})

z = Z()
print(dir(Z))
z.class_say()
z.class_talk()

# 元类演示

# 元类写法固定，必须继承自type
# 元类一般命名以MetaClass结尾

class StudyMetaClass(type):
    # 注意一下写法
    def __new__(cls, name, bases,attrs):
        # 自己的业务处理
        print('asdfasdfxcv123213123')
        attrs['id'] = '0000000'
        attrs['addr'] = 'fuck'
        return type.__new__(cls,name,bases,attrs)

# 元类定义完就可以使用，使用注意写法
class Teacher(object,metaclass=StudyMetaClass):
    pass

t = Teacher()
print(t.id)













