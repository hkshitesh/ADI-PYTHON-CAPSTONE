def my_decorator(func):
    def wrapper():
        print("Decorator has modified my_function output")
    
    return wrapper


@my_decorator
def my_function():
    print("Function is called")

# Calling my_function will now include the decorator's behavior
my_function()
