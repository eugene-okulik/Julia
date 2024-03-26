string_1 = 'результат операции: 42'
string_2 = 'результат операции: 514'
string_3 = 'результат работы программы: 9'

# print(string_1.index('42'))
# print(string_2.index('514'))
# print(string_3.index('9'))

# print(int(string_1[20:]) + num)
# print(int(string_2[20:]) + num)
# print(int(string_3[27:]) + num)

# print(string_1.index(':'))
# print(string_3.index(':'))
#
# print(int(string_1[19:]) + 10)
# print(int(string_2[19:]) + 10)
# print(int(string_3[27:]) + 10)


index1 = (string_1.index(':')+1)
print(int(string_1[index1:]) + 10)

index2 = (string_2.index(':')+1)
print(int(string_2[index2:]) + 10)

index3 = (string_3.index(':')+1)
print(int(string_3[index3:]) + 10)
