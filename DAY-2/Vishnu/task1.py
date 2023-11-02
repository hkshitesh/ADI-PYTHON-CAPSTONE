def my_decorator(func):
    def inner():
        print("Decorator had modified my_function output")
    return inner

@my_decorator
def my_function():
    print("Function is called")

my_function()