text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, "
        "facilisis vitae semper at, dignissim vitae libero”")

words = text.split()
fin_words = []
for word in words:
    if 'ing' in word:
        fin_words.append(word.replace(',ing', 'ing,',))
    else:
        fin_words.append(word.replace(',ing', 'ing,' + 'ing'))

    print(' ' .join(fin_words))
