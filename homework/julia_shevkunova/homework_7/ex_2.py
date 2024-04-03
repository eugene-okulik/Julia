words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
a, b, c, d = words


def print_keу(words):
    if words == a:
        print(words * 3)
    elif words == b:
        print(words * 5)
    elif words == c:
        print(words * 1)
    elif words == d:
        print(words * 50)


print_keу(a)
print_keу(b)
print_keу(c)
print_keу(d)
