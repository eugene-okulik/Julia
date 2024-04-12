def fib(n):
    a, b = 0, 1000001
    for __ in range(n):
        yield a
        a, b = b, a + b


count = 1
for number in fib(1000001):
    if count == 5:
        print(number)
    if count == 200:
        print(number)
    if count == 1000:
        print(number)
    if count == 100000:
        print(number)
    count += 1
