# Decorator Pattern
def my_decorator(func):
    def wrap_func(x):
        print('****')
        func(x)
        print('****')
    return wrap_func

@my_decorator
def hello(greeting):
    print(greeting)
    

hello('hiii')