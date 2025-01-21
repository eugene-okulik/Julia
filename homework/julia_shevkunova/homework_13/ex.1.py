import os
import datetime

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

now = datetime.datetime.now()

with open(eugene_file_path) as data_txt:
    print(data_txt.read())
print("_________________________________")


def process_date_strings(eugene_file_path):
    with open(eugene_file_path) as data_txt:
        for line in data_txt:
            if line.startswith('1.'):
                date_str = line[3:29]
                dt_obj = datetime.datetime.fromisoformat(date_str)
                new_dt = dt_obj + datetime.timedelta(weeks=1)
                print(new_dt)
            if line.startswith('2.'):
                date_str = line[3:29]
                dt_obj = datetime.datetime.fromisoformat(date_str)
                print(dt_obj.strftime("%A"))
            if line.startswith('3.'):
                date_str = line[3:29]
                dt_obj = datetime.datetime.fromisoformat(date_str)
                new_dt = now - dt_obj
                print(new_dt)


process_date_strings(eugene_file_path)
