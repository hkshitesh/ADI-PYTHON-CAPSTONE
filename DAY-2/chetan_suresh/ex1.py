import time

def slow_function_decorator(func):
    def inner():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"time taken by {func.__name__} : {end_time - start_time: .6f} seconds")
        return result
    return inner


@slow_function_decorator
def slow_function10():
    time.sleep(10)
    return "Operation Completed"

@slow_function_decorator
def slow_function5():
    time.sleep(5)
    return "Operation Completed"

res = slow_function5()
print(res)