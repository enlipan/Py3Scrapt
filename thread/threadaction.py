import threading
import time


def takeANap():
    time.sleep(3)
    print('wake up')
    pass


threadObj = threading.Thread(target=takeANap)
# threadObj = threading.Thread(target=takeANap())  注意比较执行差异  直接执行了 takeANap 函数
threadObj.start()

print('end main')
