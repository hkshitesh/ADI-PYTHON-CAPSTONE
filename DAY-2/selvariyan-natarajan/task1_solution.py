

def my_decorator(func):
    def inner_func():
        return "Decorator modified output"

    return inner_func


@my_decorator
def my_function():
    return "Function is called"


print(my_function())