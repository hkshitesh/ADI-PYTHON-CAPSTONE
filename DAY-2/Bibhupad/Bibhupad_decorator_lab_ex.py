

def decorator_function(func):
    def inner():
        result = func()
        print ("Decorator added")
        return result

    return inner

@decorator_function
def my_function():
    return "function is called."

res = my_function()
print(res)