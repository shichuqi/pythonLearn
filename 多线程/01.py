import time

# 先使用 旧包 _thread 不推荐，此处只是例子
import _thread as thread

def taskJobOne():
    print('start time is {0}'.format(time.ctime()))
    time.sleep(2)
    print('stop time is {0}'.format(time.ctime()))
    return None

def taskJobTwo():
    print('start time is {0}'.format(time.ctime()))
    time.sleep(2)
    print('stop time is {0}'.format(time.ctime()))
    return None


def main():
    print('main start time is {0}'.format(time.ctime()))
    thread.start_new(taskJobOne,())
    thread.start_new(taskJobTwo,())
    print('main stop time is {0}'.format(time.ctime()))

if __name__ == '__main__':
    main()
    time.sleep(4)
