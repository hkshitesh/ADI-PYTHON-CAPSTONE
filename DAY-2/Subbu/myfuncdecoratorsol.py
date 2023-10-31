def my_decorator(func):
    def inner():
        result = func()
        print("My Decorator had modified my_function output")
        return result
    return inner

@my_decorator
def my_function():
    return "Function is called"

res = my_function()
print(res)











