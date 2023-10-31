
def my_decorator(fun):
    def decorator_fun():
        return "Decorator had modified my_function output"

    return decorator_fun

@my_decorator
def my_function():
    print("Function is Called")
    return

print(my_function())
