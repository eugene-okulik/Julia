def repeat_me(func):
    def wrapper():
        func()
        func()

    return wrapper


@repeat_me
def funcdec():
    print('print me')


funcdec()
