class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.setName(name)
        self.setAge(age)

    def intro(self):
        print('my name is {0},my age is {1}'.format(self.name,self.age))

    def setName(self,name):
        self.name = name.upper()

    def setAge(self,age):
        self.age = int(age)
    
s1 = Student('aaa',24.7)
s1.intro()

# property案例
# 输入任何名字都是大写
# 输入名字，都是整数保存
class Person():
    '''sdfasdfasdfasdf'''
    # 名字可以随意
    def fget(self):
        return self._name * 2
    def fset(self,name):
        self._name = name.upper()
    def fdel(self):
        self._name = 'None'

    def __call__(self, *args, **kwargs):
        print("call被调用",*args)
        print(type(args))
        print(type(kwargs))
        return None
    def __str__(self):
        return '123123123213'
    name = property(fget,fset,fdel,'duisadfafd')

p1 = Person()
p1.name = 'aaaa'
print(p1.name)


print("$"*20)
# 类的内置函数
print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)

print("$"*20)
# __call__
p1('aa',{'aa':12})

print("$"*20)
# __str__
print(p1)
# __repr__
print(p1.__repr__())
#__getattr__
class A():
    def __getattr__(self,name):
        print("no find")
        print(name)

a = A()
print(a.name)

print('#'*20)

# __setattr__
class B():
    def __init__(self):
        pass
    def __setattr__(self,name,value):
        print('设置属性：{0}'.format(name))
        # 下面语句会导致死循环
        # self.name = value
        #此时，规定统一调用父类魔法函数
        super().__setattr__(name,value)
p = B()
p.__setattr__('aa','111')
print(p.__dict__)
p.age = 18

print("%"*20)

# __gt__
class Student():
    def __init__(self,name):
        self._name = name

    def __gt__(self, other):
        print('asdfasdf{0}>{1}?'.format(self,other))
        return self._name > other._name

stu1 = Student("one")
stu2 = Student("two")
print(stu1 > stu2)

# 三种方法案例
class PP():
    # 实例方法
    def eat(self):
        print(self)
        print('eat...')
    # 类方法
    @classmethod
    def play(cls):
        print(cls)
        print('play...')
    # 静态方法
    # 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print('say...')

yueyue = PP()
# 实例方法
yueyue.eat()
# 类方法
PP.play()
yueyue.play()
# 静态方法
PP.say()
yueyue.say()











