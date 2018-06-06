# 类继承的语法
    # 在python中，任何类都有一个共同的父类叫object

# 父类
class Person():
    name = "NoName"
    age = 0
    _petname = 'sec' # 小名，是受保护的，子类可以用，不能公用
    __score = 0 # 成绩，是秘密，只能自己调用
    def sleep(self):
        print('Sleeping ......')
        return None
    def work(self):
        print('work')
        return None
    def work2(self):
        print('work2')
        return None
# 子类
class Teacher(Person):
    def make_test(self):
        pass
    def sleep(self):
        print("no")
        pass
    def work(self):
         # 扩充父类的功能，只需调用父类相应的函数
        Person.work(self)
        self.sleep()
        pass
    def work2(self):
        # 扩充父类的功能，还可以用super()
        super().work2()
        pass

    

t = Teacher()
print(t.name)
print(Teacher.name)

print(t._petname)
print(t._Person__score)
t.sleep()

t.work()
t.work2()


print("@"*20)
# 构造函数


class Animel():
    def __init__(self):
        print('Animel')
    pass

class PaxingAni(Animel):
    pass


class Dog(PaxingAni):
    def __init__(self,name):
        # 每次实例化的时候，第一个被自动调用
        # 主要进行初始化
        print('dog{0}'.format(name))
        pass

kaka = Dog('aaa')
aa = PaxingAni()

print("@"*20)
# super
print(type(super))
help(super)