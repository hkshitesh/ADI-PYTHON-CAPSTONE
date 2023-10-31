def sample_decarator(func):
    def inner_function():
        return "Decorator modified output"
    return inner_function


@sample_decarator
def print_function():
    return "Function is called"


res= print_function()
print(res)
