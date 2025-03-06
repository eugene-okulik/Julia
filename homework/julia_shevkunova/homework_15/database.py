import mysql.connector as mysql


db = mysql.connect(
    username='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port='25060',
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# добавляем студента
cursor.execute("INSERT INTO students (name, second_name) VALUES ('JuliS', 'Test2')")

# берем id студента
student_id = cursor.lastrowid

# добавляем группу
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('QA1234', 'oct 12', 'dec 13')")
group_id = cursor.lastrowid

# обновляем студента, добавляя группу
cursor.execute("UPDATE students SET group_id=%s WHERE id=%s", (group_id, student_id))

# добавляем книги
insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('First book', student_id),
        ('Second', student_id)
    ]
)
# добавляем учебные предметы
insert_query = "INSERT INTO subjets (title) VALUES (%s)"
cursor.executemany(
    insert_query, [
        ('Basics of programming',),
        ('Architecture',)
    ]
)
# берем subjets_id
subjets_id = cursor.lastrowid

# добавляем занятия по предметам
insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('Variables-2', subjets_id),
        ('Operators-2', subjets_id),
        ('Components of Web applications-2', subjets_id),
        ('Building Application-2', subjets_id)
    ]
)

# берем lesson_id
lesson_id = cursor.lastrowid

# добавляем оценки по занятиям
insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        (4, lesson_id, student_id),
        (5, lesson_id, student_id),
        (7, lesson_id, student_id),
        (10, lesson_id, student_id)
    ]
)

# выводим все оценки студента
cursor.execute("SELECT value FROM marks WHERE student_id =%s", (student_id,))
print(cursor.fetchall())

# выводим все книги, которые находятся у студента
cursor.execute("SELECT title FROM books WHERE taken_by_student_id=%s", (student_id,))
print(cursor.fetchall())

# выводим группу студента, книги, оценки с названиями занятий и предметов
cursor.execute("""
    SELECT s.name as 'student', g.title as 'group', b.title as 'book name', m.value as 'mark', l.title as 'lesson',\
     s2.title as 'subject'
    FROM students s
    JOIN books b ON s.id=b.taken_by_student_id
    JOIN marks m ON s.id=m.student_id
    JOIN `groups` g ON g.id=s.group_id
    JOIN lessons l ON l.id=m.lesson_id
    JOIN subjets s2 ON s2.id=l.subject_id
    WHERE s.id=%s AND l.id=%s AND g.id=%s AND s2.id=%s
    """, (student_id, lesson_id, group_id, subjets_id))
print(cursor.fetchall())
db.commit()
db.close()
