import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.csv')
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')


with open(eugene_file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    for row in file_data:
        if db.is_connected():
            cursor.execute("""
           SELECT s.name as 'name', s.second_name as 'second_name', g.title as 'group', b.title as 'book name', \
           s2.title as 'subject', l.title as 'lesson', m.value as 'mark'
           FROM students s
           JOIN books b ON s.id=b.taken_by_student_id
           JOIN marks m ON s.id=m.student_id
           JOIN `groups` g ON g.id=s.group_id
           JOIN lessons l ON l.id=m.lesson_id
           JOIN subjets s2 ON s2.id=l.subject_id
           """)
            result_list = cursor.fetchall()
            for row_one in result_list:
                values_list = list(row_one.values())
            try:
                if row not in values_list:
                    print(row)
            except Exception as e:
                    print(f"{row}: {e}")

    cursor.close()
    db.close()
