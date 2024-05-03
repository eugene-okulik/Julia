def operations(func):
    def wrapper():
        if input1 == input2:
            return func(input1, input2, '+')
        if input1 > input2:
            return func(input1, input2, '-')
        if input2 > input1:
            return func(input1, input2, '/')
        if input2 < 0 or input1 < 0:
            return func(input1, input2, '*')
        else:
            pass

    return wrapper


@operations
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        pass


input1 = int(input('введите число1 '))
input2 = int(input('введите число2 '))

calc()
result = calc()
print(result)
