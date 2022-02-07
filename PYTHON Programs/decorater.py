def my_decorater(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func()
@my_decorater
def hello():
       print('hello')  