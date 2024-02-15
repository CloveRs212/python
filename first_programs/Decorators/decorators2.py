# Decorator
def my_decorator(func):
    def wrap_func():
        print('****')
        func()
        print('****')
    return wrap_func

@my_decorator
def hello():
    print('hellloooo')
    
@my_decorator
def bye():
    print('see you later')

hello()
bye()
## it will take a func that you want to be wrapped and call it inside. Using @my_decorator will wrap hello and bye with  the other functions. Then it returns the function all together as determined by the code.