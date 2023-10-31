import time

def my_decorator(func):
    def inner():
        
        result = func()
        
        print('Decorator has modified fn output')
        return result
    return inner

@my_decorator
def my_function():
    print('Function has been called')

res= my_function()
print(res)
