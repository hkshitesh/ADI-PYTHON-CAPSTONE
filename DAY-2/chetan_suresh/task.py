def my_decorator(func):
    def inner():
        return "Decorator is called"
    return inner

@my_decorator
def my_function():
    return "Function is called"

print(my_function())