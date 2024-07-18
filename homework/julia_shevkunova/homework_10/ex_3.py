def operations(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        if first > second:
            return func(first, second, '-')
        if second > first:
            return func(first, second, '/')
        if second < 0 or first < 0:
            return func(first, second, '*')
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

calc(input1, input2)
result = calc(input1, input2)
print(result)
