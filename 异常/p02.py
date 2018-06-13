try:
    num = int(input("please input your number:"))
    result = 100/num
    print(result)

except ZeroDivisionError as e:
    print('ZeroDivisionError')
    print(e)
    exit()

except NameError as e:
    print('NameError')
    print(e)
    exit()
except Exception as e:
    print('exception')
    print(e)
    exit()

print(num)
