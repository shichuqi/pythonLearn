# 自定异常

class MyError(Exception):
    pass


try:
    print('helloworld')
    raise MyError('MyError')
except MyError as e:
    print(e)



# else 案例
try:
    num = int(input("please input your number:"))
    result = 100/num
    print(result)
except Exception as e :
    print(e)
else:
    print('noException')
finally:
    print('see you again')