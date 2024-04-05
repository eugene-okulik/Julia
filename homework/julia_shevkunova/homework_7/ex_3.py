string_1 = 'результат операции: 42'
string_2 = 'результат операции: 514'
string_3 = 'результат работы программы: 9'
string_4 = 'результат: 2'

index1 = (string_1.index(':') + 1)
num_1 = int(string_1[index1:])
index2 = (string_2.index(':') + 1)
num_2 = int(string_2[index2:])
index3 = (string_3.index(':') + 1)
num_3 = int(string_3[index3:])
index4 = (string_4.index(':') + 1)
num_4 = int(string_4[index4:])


def sum_numbers(index):
    print(index + 10)


sum_numbers(num_1)
sum_numbers(num_2)
sum_numbers(num_3)
sum_numbers(num_4)
