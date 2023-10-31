def my_decorator(func):
    def wrapper():
        print("Decorator had modified my_function output")

    return wrapper


@my_decorator
def my_function():
    print("Function is called")


my_function()
