

def my_decorator(func):
    def inner():
       rs = func()
       return "Decorator had modified my function output"
    return inner

@my_decorator
def my_function():
    return "Function is called"

res = my_function()
print(res)

