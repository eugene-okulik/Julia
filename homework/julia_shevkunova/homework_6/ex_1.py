text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')

words = text.split()
fin_words = []
ending = 'ing'
for word in words:
    fin_words.append(word + ending)


result = ' '.join(fin_words).replace(',ing', 'ing,').replace('.ing', 'ing.')
print(result)
