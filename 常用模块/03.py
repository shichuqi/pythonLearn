# random
# 随机数  - 所有的随机模块是伪随机
import random ,time
t1 = time.time()
print(t1)
while(True):
    num = int(random.random()*100)
    if num == 99:
        print(num)
        break
print(float(time.time() - t1))


# randint随机生成指定范围随机数，包含左右
print(random.randint(0,100))