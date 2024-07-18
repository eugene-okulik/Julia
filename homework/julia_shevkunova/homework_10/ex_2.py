def repeat_me(func):
    def wrapper(count):
        for i in range(count):
            func(count)

    return wrapper


@repeat_me
def funcdec(count):
    print('print me')


funcdec(5)


