# raise 手动引发异常

try:
    print('hello world')
    raise Exception('9999')

except Exception as e :
    print(e)
    print('Exception')

finally:
    print('continue')