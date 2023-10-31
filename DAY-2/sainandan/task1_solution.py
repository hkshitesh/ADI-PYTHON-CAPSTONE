"""
Task 1 solution
"""

def my_function_decorator(fun):
    """
    Decorater to modify the output of my_function()
    """
    def inner():
        print("Decorator has modified my function output")
        result = fun()
        return result
    return inner

@my_function_decorator
def my_function():
    """
    My function that returns a string when called
    """
    return "Function is called"

RESULT = my_function()
print(RESULT)
