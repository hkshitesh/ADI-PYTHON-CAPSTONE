def func_decorator(func):
    def wrapper():
        return "Decorator is decorated\nFunction overriden"
    return wrapper


@func_decorator
def my_function():
    return "Function is called"


result = my_function()
print(result)
