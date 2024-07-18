def repeat_me(func):
    def wrapper(count):
        for i in range(count):
            func()

    return wrapper


@repeat_me
def funcdec():
    print('print me')


funcdec(2)
