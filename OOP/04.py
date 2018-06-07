class A():
    pass

class B(A):
    pass
# __mro__显示家谱
print(A.__mro__)
print(B.__mro__)

print('$'*20)

# 多继承的例子
# 子类可以直接调用父类的属性和方法
class Fish():
    def __init__(self,name):
        self.name = name

    def swim(self):
        print('i am swimming......')
        return None


class Bird():
    def __init__(self,name):
        self.name = name

    def fiy(self):
        print('i am flying...')
        return None

class Person():
    def __init__(self,name):
        self.name = name

    def work(self):
        print('i am working...')
        return None

class SuperMan(Person,Bird,Fish):
    def __init__(self, name):
        self.name = name


s = SuperMan("yueyue")
s.fiy()
s.swim()

print('#'*20)
# 单继承例子
class Student(Person):
    def __nit__(self,name):
        self.name = name

stu = Student('yueyue')
stu.work()

# 构造函数例子
class P():
    # 对这个P进行实例化的时候
    # 确定某个具体对象时
    def __init__(self):
        self.name = 'noName'
        self.age = 18
        self.address = 'noWhere'

    pass
# 实例化时确定某一个P
p = P()
print(p.__dict__)

print('#'*20)

#### Mixin例子
class Man():
    def eat(self):
        print('eat')

# 此时不继承man
class TeacherMixin():
    def work(self):
        print('work')

# 此时不继承man
class StudentMixin():
    def study(self):
        print('study')

class TutorM(Man,TeacherMixin,StudentMixin):
    pass

tt = TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)
print('#'*20)
# issubclass

class H():
    pass
class G(H):
    age = 18
    pass
class J():
    pass
print(issubclass(G,H))
print(issubclass(J,H))
print('#'*20)
# isinstance
g = G()
print(isinstance(g,G))
print('#'*20)
# hasattr
print(hasattr(g,'name'))
print(hasattr(g,'age'))
print('#'*20)
# getattr
print(getattr(g,'age'))
print('#'*20)
# setattr
setattr(g,'name','aaa')
print(getattr(g,'name'))















