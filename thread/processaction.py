import multiprocessing


def process(num):
    print(str(multiprocessing.current_process()))
    print(str(num))


for i in range(5):
    pro = multiprocessing.Process(target=process, args=(i,))
    pro.start()

print('cpuCount:' + str(multiprocessing.cpu_count()))


class MyProcess(multiprocessing.Process):
    def __init__(self):
        pass

    def run(self):
        pass
