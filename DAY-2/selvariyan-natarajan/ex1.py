import time


def time_it(func):
    def inner_func():
        start = time.time()
        r = func()
        stop = time.time()
        print(f"time taken by {func.__name__} : {stop-start : .6f} sec")
        return r
    
    return inner_func


@time_it
def slow_function5():
    time.sleep(5)
    return "Operation Completed"


@time_it
def slow_function10():
    time.sleep(10)
    return "Operation Completed"


print(slow_function10())
print(slow_function5())
