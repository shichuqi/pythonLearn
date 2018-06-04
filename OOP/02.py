######
class A():
    name = 'dana'
    age = 18

    def say(self):
        self.name = "aaaaa"
        self.age = 200
        return None

# 不对对象初赋值的前提下，对象的实例的属性指向类实例
# A称为类的实例
print(A.name)
print(A.age)

print('*'*20)

print(id(A.name))
print(id(A.age))

print("*"*20)

a = A()

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print("*"*20)
# 查看A内所有的属性
print(A.__dict__)
print(a.__dict__)
a.name = 'bbb'
a.age = 19
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print(a.__dict__)

print("*"*20)
a.name = 'ccc'
a.age = 20
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print("*"*20)
######
class Student():
    name = 'dana'
    age = 18

    def say(self):
        self.name = "aaaaa"
        self.age = 200
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
        return None


yueyue = Student()
yueyue.say()

print("*"*20)
#####
class Teacher():
    name = 'dana'
    age = 19

    def say(self):
        self.name = "youyou"
        self.age = 20
        print(self.name,":",__class__.age)

    def sayAgain():
        # 调用类的成员变量要用__class__
        print(__class__.name, ":",__class__.age)
        print("hello world")


t = Teacher()
t.say()
Teacher.sayAgain()
print('*'*20)

#####
class X():
    name = 'dana'
    age = 18
    #构造方法，只针对对象，类不变
    def __init__(self):
        self.name = 'woshi'
        self.age = 24


    def say(self):
        print(self.name,':',self.age)

class Y():
    name = 'bbb'
    age = 90

x = X()
x.say()
X.say(x)
X.say(X)
X.say(Y)
# 以上代码，利用鸭子模型
print('*'*20)
print('*'*20)
#########
class Person():
    # name是公共成员
    name = 'liuying'
    # __age就是私有成员
    __age = 18

person = Person()
# name是共有
print(person.name)
# age是私有的
## print(person.__age)   AttributeError: 'Person' object has no attribute '__age'
## 可以使用对象._classname_attributename访问
print(Person.__dict__)

# Python中的私有变量其实是被改名了，并非真正的私有
print(person._Person__age)


