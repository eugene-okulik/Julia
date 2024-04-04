words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
# a, b, c, d = words


def print_keу(words):
    for word, count in words.items():
        print(word * count)


print_keу(words)
