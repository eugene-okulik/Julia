num = 5

while True:
    user_input = int(input('угадай цифру: '))
    if user_input != 5:
        print('Попробуйте снова')
        continue
    elif user_input == 5:
        print('Поздравляю! Вы угадали')
        break
