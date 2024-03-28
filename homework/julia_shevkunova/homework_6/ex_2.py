range_e = (1, 101)

for number in range_e:
    if number % 3 == 0:
        print('Fuzz')
    if number % 5 == 0:
        print('Buzz')
    elif number % 5 == 0 and number % 3 == 0:
        print('FuzzBuzz')
else:
    print(number)
