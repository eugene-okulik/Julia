import random

salary = int(input('Your salary? '))
bonus = bool(random.random())

if bonus:
    salary_with_bonus = bonus + salary
    print(salary, bonus, '-$' + str(salary_with_bonus))
else:
    salary_withot_bonus = salary
    print(salary, bonus, '-$' + str(salary))
