
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22,
                22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


def hot_days(x):
    return x > 28


new_list = filter(hot_days, temperatures)
new_list_2 = (list(new_list))

print(max(new_list_2))
print(min(new_list_2))
print(sum(new_list_2)/len(new_list_2))
